from django.urls import path

from ProyectoWebApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('tienda', views.tienda, name="Tienda"),
    path('blog', views.blog, name="Blog"),
    path('contacto', views.contacto, name="Contacto"),
    path('login', views.login, name="Login"),
    path('registro', views.registro, name="Registro"),
]