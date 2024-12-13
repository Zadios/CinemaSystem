from Applications.Showtime.models import Ticket  # Ajusta el nombre del modelo según tu sistema
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect


def index(request):
    return render(request, 'adminpanel/adminpanel.html')  # Llama a una plantilla HTML

def ticket_list(request):
    tickets = Ticket.objects.all()  # Obtiene todos los tickets
    return render(request, 'adminpanel/ticket_list.html', {'tickets': tickets})

def mark_as_delivered(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.status = False  # Cambiar a entregado (es decir, poner el estado como False)
    ticket.save()
    return redirect('adminpanel:ticket_list')  # Redirigir a la lista de tickets

def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.delete()
    return redirect('adminpanel:ticket_list')  # Redirigir a la lista de tickets
