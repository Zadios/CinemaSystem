from django.urls import path
from . import views

app_name = 'adminpanel'

urlpatterns = [
    path('', views.index, name='adminpanel'),  # Ruta para la vista principal del panel
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/<int:ticket_id>/deliver/', views.mark_as_delivered, name='mark_as_delivered'),
    path('tickets/<int:ticket_id>/delete/', views.delete_ticket, name='delete_ticket'),
]

