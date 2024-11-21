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
    # Obtener el show y asignar el show_code a la sesión
    show = get_object_or_404(Show, pk=show_id)
    
    # Limpiar las promociones anteriores de la sesión (solo si la clave existe)
    if request.session.get('selected_promotions') is not None:
        request.session.pop('selected_promotions', None)

    # Guardar show_id en la sesión
    request.session['show_id'] = show.show_code
    print(f"Show ID guardado en sesión: {request.session['show_id']}")

    if request.method == "POST":
        print(request.POST)
        
        # Obtener las promociones seleccionadas y las cantidades
        promociones = request.POST.getlist('promociones')
        cantidades = request.POST.getlist('cantidades')

        # Verificar si hay promociones seleccionadas
        if promociones:
            request.session['selected_promotions'] = promociones
            print(f"Promociones guardadas en sesión: {request.session['selected_promotions']}")

        # Filtrar las promociones seleccionadas para guardar solo las de cantidad mayor a 0
        if promociones and cantidades:
            selected_promotions = {}

            for promo, cantidad in zip(promociones, cantidades):
                cantidad = int(cantidad)
                if cantidad > 0:
                    selected_promotions[promo] = cantidad

            # Guardar las promociones seleccionadas en la sesión solo si hay alguna con cantidad > 0
            if selected_promotions:
                request.session['selected_promotions'] = selected_promotions
                print(f"Datos almacenados en sesión: {request.session['selected_promotions']}")
            else:
                print("No se seleccionaron promociones con cantidad mayor a 0")

        # Redirigir al pago
        return redirect('showtime:pago')

    context = {'show': show}
    return render(request, 'showtime/comprar_entradas.html', context)


def pago(request):
    # Recuperar el show_id de la sesión
    show_id = request.session.get('show_id')
    if not show_id:
        messages.error(request, "No se pudo procesar la compra. Por favor, selecciona tus entradas nuevamente.")
        return redirect('showtime:comprar_entradas')

    # Obtener el objeto Show
    show = get_object_or_404(Show, show_code=show_id)
    print(f"Show recuperado: {show}")

    # Recuperar promociones seleccionadas de la sesión
    selected_promotions = request.session.get('selected_promotions', {})

    # Procesar POST
    if request.method == "POST":
        promociones = request.POST.getlist('promociones[]')
        cantidades = request.POST.getlist('cantidades[]')
        print(f'Promociones: {promociones}')
        print(f'Cantidades: {cantidades}')

        for promo_id, cantidad in zip(promociones, cantidades):
            selected_promotions[promo_id] = int(cantidad)

        request.session['selected_promotions'] = selected_promotions
        print(f"Promociones actualizadas en sesión: {selected_promotions}")

    form = PagoForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        total_tickets = 0
        total_price = 0
        for price_id, quantity in selected_promotions.items():
            price = get_object_or_404(Price, pk=price_id)
            total_tickets += price.ticket_quantity * quantity
            total_price += price.amount * quantity

        ticket_code = generate_ticket_code()
        ticket = Ticket.objects.create(
            ticket_code=ticket_code,
            show=show,
            total_tickets=total_tickets,
            total_price=total_price,
        )

        for price_id, quantity in selected_promotions.items():
            price = get_object_or_404(Price, pk=price_id)
            if quantity > 0:
                Ticket_Price.objects.create(ticket=ticket, price=price, quantity=quantity)

        return redirect('showtime:confirmacion', ticket_code=ticket.ticket_code)

    context = {'form': form, 'show': show}
    return render(request, 'showtime/pago.html', context)

def confirmacion(request, ticket_code):
    try:
        ticket = Ticket.objects.get(ticket_code=ticket_code)
    except Ticket.DoesNotExist:
        return HttpResponse("Ticket no encontrado", status=404)
    
    request.session.pop('selected_promotions', None)
    request.session.pop('show_id', None)
    
    return render(request, 'showtime/confirmacion.html', {'ticket': ticket})
