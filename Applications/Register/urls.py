from django.urls import path
from .views import register_view, login_view
from . import views

app_name = "register"

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', views.login_view, name='login'),
]
