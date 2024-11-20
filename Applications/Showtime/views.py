from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from Applications.Movie.models import Film
from .models import Show, Price, Ticket, Ticket_Price
from datetime import date, timedelta
from .forms import PagoForm
from Applications.Showtime.utils import generate_ticket_code
from django.contrib import messages

def horarios(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    formats = film.format.all()  # Formatos disponibles para la película
    languages = film.language.all()  # Idiomas disponibles para la película
    shows = Show.objects.filter(film=film).order_by('show_date', 'show_time')

    selected_format = request.GET.get('format')
    selected_language = request.GET.get('language')

    # Filtrar los shows solo si el valor seleccionado es un número
    if selected_format and selected_format.isdigit():
        shows = shows.filter(format_id=selected_format)
    if selected_language and selected_language.isdigit():
        shows = shows.filter(language_id=selected_language)

    # Organizar los horarios por fecha
    horarios_por_fecha = {}
    for show in shows:
        fecha = show.show_date.strftime('%Y-%m-%d')
        hora = show.show_time.strftime('%H:%M')
        if fecha not in horarios_por_fecha:
            horarios_por_fecha[fecha] = []
        horarios_por_fecha[fecha].append({
            "show_time": hora,
            "show_code": show.show_code
        })

    # Generar días desde hoy hasta el próximo miércoles
    today = date.today()
    days_until_next_wednesday = (2 - today.weekday() + 7) % 7  # 2 representa el miércoles
    days = [today + timedelta(days=i) for i in range(days_until_next_wednesday + 1 + 7)]

    context = {
        'film': film,
        'formats': formats,
        'languages': languages,
        'shows': shows,
        'days': days,
        'selected_format': selected_format,
        'selected_language': selected_language,
        'horarios_por_fecha': horarios_por_fecha,  # Pasamos el diccionario de horarios al template
    }
    return render(request, 'showtime/horarios.html', context)

def comprar_entradas(request, show_id):
    show = get_object_or_404(Show, pk=show_id)
    print(f"Método de solicitud: {request.method}")


    if request.method == "POST":
        print(request.POST)  # Muestra todos los datos enviados por el formulario
        # Obtener promociones seleccionadas y cantidades
        promociones = request.POST.getlist('promociones')  # IDs de promociones
        cantidades = request.POST.getlist('cantidades')  # Cantidades asociadas
 
        if promociones:
            request.session["promociones_seleccionadas"] = promociones
            print(f"Promociones guardadas en sesión: {request.session['promociones_seleccionadas']}")

        else:
            print("No se recibieron promociones")
        
        # Guardar en la sesión
        request.session['show_id'] = show_id
        """ request.session['selected_promotions'] = {
        promo: int(cantidad) for promo, cantidad in zip(promociones, cantidades)
        } """

        if promociones and cantidades:
            request.session['selected_promotions'] = {
            promo: int(cantidad) for promo, cantidad in zip(promociones, cantidades) if int(cantidad) > 0
        }

        print(f"Datos almacenados en sesión: {request.session['selected_promotions']}")
        # Redirigir al pago
        return redirect('showtime:pago')
    
    context = {
    'show': show,
    }

    return render(request, 'showtime/comprar_entradas.html', context)


def pago(request):
    # Recupera datos de la sesión
    show_id = request.session.get('show_id')
    
    # Recupera las promociones de la sesión
    selected_promotions = request.session.get('selected_promotions', {})

    # Si el formulario fue enviado, procesar los datos
    if request.method == "POST":
        promociones = request.POST.getlist('promociones[]')
        cantidades = request.POST.getlist('cantidades[]')
        print(f'Promociones: {promociones}')
        print(f'Cantidades: {cantidades}')
        
        # Asegúrate de que el número de promociones y cantidades coincidan
        for promo_id, cantidad in zip(promociones, cantidades):
            selected_promotions[promo_id] = int(cantidad)  # Asignamos la cantidad a cada promoción
        
        # Guardar las promociones actualizadas en la sesión
        request.session['selected_promotions'] = selected_promotions
        print(f"Promociones actualizadas en sesión: {selected_promotions}")

    if not show_id:
        messages.error(request, "No se pudo procesar la compra. Por favor, selecciona tus entradas nuevamente.")
        return redirect('showtime:comprar_entradas', show_id=show_id)

    show = get_object_or_404(Show, pk=show_id)
    form = PagoForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # Calcular totales
        total_tickets = 0
        total_price = 0
        for price_id, quantity in selected_promotions.items():
            price = get_object_or_404(Price, pk=price_id)
            total_tickets += price.ticket_quantity * quantity
            total_price += price.amount * quantity

        # Crear el ticket
        ticket_code = generate_ticket_code()
        ticket = Ticket.objects.create(
            ticket_code=ticket_code,
            show=show,
            total_tickets=total_tickets,
            total_price=total_price,
        )

        # Registrar las promociones asociadas al ticket
        for price_id, quantity in selected_promotions.items():
            price = get_object_or_404(Price, pk=price_id)
            Ticket_Price.objects.create(ticket=ticket, price=price, quantity=quantity)

        # Redirigir a la confirmación
        return redirect('showtime:confirmacion', ticket_code=ticket.ticket_code)

    context = {'form': form, 'show': show}
    return render(request, 'showtime/pago.html', context)





def confirmacion(request, ticket_code):
    try:
        ticket = Ticket.objects.get(ticket_code=ticket_code)
    except Ticket.DoesNotExist:
        return HttpResponse("Ticket no encontrado", status=404)
    
    return render(request, 'showtime/confirmacion.html', {'ticket': ticket})
