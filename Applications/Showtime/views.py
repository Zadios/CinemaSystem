from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Show, Price, Ticket

def listar_compra(request, show_id):
    # Obtén el show correspondiente
    show = get_object_or_404(Show, pk=show_id)

    # Datos adicionales relacionados
    film = show.film
    movie_theater = show.movie_theater
    prices = show.prices.all()

    # Contexto para el template
    context = {
        'show': show,
        'film': film,
        'movie_theater': movie_theater,
        'prices': prices,
    }

    return render(request, 'Showtime/compra.html', context)


def procesar_compra(request, show_id, cantidad_entradas, price_id):
    # Obtener los objetos show y price
    show = Show.objects.get(id=show_id)
    price = Price.objects.get(id=price_id)
    
    # Calcular el precio total
    total_precio = cantidad_entradas * price.amount
    
    # Crear el ticket
    ticket = Ticket.objects.create(
        show_code=show,
        price=price,
        ticket_quantity=cantidad_entradas
    )
    
    # Retornar respuesta o redirigir
    return JsonResponse({'ticket_code': ticket.ticket_code, 'total_precio': total_precio})