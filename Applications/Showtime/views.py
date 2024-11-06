from django.shortcuts import render, get_object_or_404
from Applications.Movie.models import Film, Format, Language
from .models import Show, Movie_Theater

def comprar_entradas(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    formats = film.format.all()  # Formatos disponibles para la película
    languages = film.language.all()  # Idiomas disponibles para la película
    shows = Show.objects.filter(film=film)

    selected_format = request.GET.get('format')
    selected_language = request.GET.get('language')

    # Filtrar los shows por formato e idioma, si están seleccionados
    if selected_format:
        shows = shows.filter(format_id=selected_format)
    if selected_language:
        shows = shows.filter(language_id=selected_language)

    context = {
        'film': film,
        'formats': formats,
        'languages': languages,
        'shows': shows,
        'selected_format': selected_format,
        'selected_language': selected_language,
    }
    return render(request, 'showtime/comprar_entradas.html', context)