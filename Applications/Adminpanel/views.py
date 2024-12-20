from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from Applications.Showtime.models import Ticket

def superuser_required(view_func):
    """
    Decorador para restringir vistas solo a superusuarios.
    Si el usuario no es superusuario, devuelve un error 404.
    """
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:  # Si el usuario no está autenticado
            raise Http404("Página no encontrada")  # Lanzar error 404
        if not request.user.is_superuser:  # Si no es superusuario
            raise Http404("Página no encontrada")  # Lanzar error 404
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@superuser_required
def admin(request):
    return render(request, 'adminpanel/adminpanel.html')

@superuser_required
def ticket_list(request):
    search_query = request.GET.get('search', '')  # Obtener el término de búsqueda del parámetro GET
    if search_query:
        tickets = Ticket.objects.filter(ticket_code__icontains=search_query)  # Filtrar tickets por código
    else:
        tickets = Ticket.objects.all()  # Mostrar todos los tickets si no hay búsqueda
    return render(request, 'adminpanel/ticket_list.html', {'tickets': tickets})

@superuser_required
def mark_as_delivered(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.status = False  # Cambiar a entregado
    ticket.save()
    return redirect('adminpanel:ticket_list')  # Redirigir a la lista de tickets

@superuser_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.delete()
    return redirect('adminpanel:ticket_list')  # Redirigir a la lista de tickets
