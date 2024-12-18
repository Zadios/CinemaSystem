from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, login_view, profile_view
from . import views

app_name = "register"

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='register:login'), name='logout'),
]
