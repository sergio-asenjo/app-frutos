"""frutos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appfrutos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio_vista),
    path('listado_despachos/', views.listar_pedidos_vista),
    path('registro_despacho/', views.registro_despacho_vista),
    path('registro_despacho_exitoso/', views.registro_despacho_exitoso_vista),
    path('eliminar_despacho/', views.eliminar_despacho_vista),
    path('eliminado_despacho_exitoso/', views.eliminar_despacho_exitoso_vista),
    path('actualizar_despacho/', views.actualizar_despacho_vista),
    path('actualizado_exitoso/', views.actualizado_exitoso_vista),
]