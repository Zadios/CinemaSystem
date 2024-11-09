from django.shortcuts import render, get_object_or_404
from Applications.Movie.models import Film, Format, Language
from .models import Show, Movie_Theater

def horarios(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    formats = film.format.all()  # Formatos disponibles para la película
    languages = film.language.all()  # Idiomas disponibles para la película
    shows = Show.objects.filter(film=film).order_by('show_date', 'show_time')

    selected_format = request.GET.get('format')
    selected_language = request.GET.get('language')

    # Filtrar los shows por formato e idioma, si están seleccionados
    if selected_format:
        shows = shows.filter(format_id=selected_format)
    if selected_language:
        shows = shows.filter(language_id=selected_language)

    # Organizar los horarios por fecha
    horarios_por_fecha = {}
    for show in shows:
        fecha = show.show_date.strftime('%Y-%m-%d')
        hora = show.show_time.strftime('%H:%M')
        if fecha not in horarios_por_fecha:
            horarios_por_fecha[fecha] = []
        horarios_por_fecha[fecha].append(hora)

    context = {
        'film': film,
        'formats': formats,
        'languages': languages,
        'shows': shows,
        'selected_format': selected_format,
        'selected_language': selected_language,
        'horarios_por_fecha': horarios_por_fecha,  # Pasamos el diccionario de horarios al template
    }
    return render(request, 'showtime/horarios.html', context)

def comprar_entradas(request, show_id):
    # Obtener el show específico usando el show_id
    show = get_object_or_404(Show, pk=show_id)

    # Contexto para el template: puedes pasar cualquier dato necesario para la compra
    context = {
        'show': show,
    }
    return render(request, 'showtime/comprar_entradas.html', context)