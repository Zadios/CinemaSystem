from django.shortcuts import render, get_object_or_404, redirect
from Applications.Movie.models import Film, Format, Language
from .models import Show, Movie_Theater
from datetime import date, timedelta
from .forms import PagoForm

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
    
    if request.method == "POST":
        # Lógica para manejar la selección de entradas, p.ej., almacenar en la sesión
        # Ejemplo de almacenamiento temporal en la sesión:
        request.session['selected_show'] = show_id
        # Puedes almacenar más información aquí si lo necesitas.
        
        # Redirigir a la página de pago
        return redirect('showtime:pago')
    
    context = {
        'show': show,
    }
    return render(request, 'showtime/comprar_entradas.html', context)


def pago(request):
    if request.method == "POST":
        form = PagoForm(request.POST)
        if form.is_valid():
            # Procesar el pago aquí (ej., guardar en base de datos o enviar a una pasarela de pagos)
            # Luego redirigir a una página de confirmación o a la vista final.
            return redirect('showtime:confirmacion')
    else:
        form = PagoForm()

    context = {'form': form}
    return render(request, 'showtime/pago.html', context)
