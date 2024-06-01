"""
URL configuration for ClinicaJamesMichael project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from ClinicaJmaesMichaelApp.views import Logueo,RegistroUsuario,Pacientes,ConsultaMedica,registroEnfermeras

urlpatterns = [
    path('logueo',Logueo.as_view(),name="login"),
    path("admin/", admin.site.urls),
    path('RH',RegistroUsuario.as_view(),name="modulo registrar rh"),
    path('RH/<id>',RegistroUsuario.as_view(),name="modulo registrar rh"), 
    path("administradores",Pacientes.as_view(),name="modulo de pacientes"),
    path('administradores/<id>',Pacientes.as_view(),name="modulo de pacientes"),
    path("historia/",ConsultaMedica.as_view(),name="Historia clinica"),
    path("historia/<id>",ConsultaMedica.as_view(),name="Historia clinica"),
    path("registroVisita",registroEnfermeras.as_view(),name="Modulo de registro visitas"),
    path("registroVisita/<id>",registroEnfermeras.as_view(),name="Modulo de registro visitas")

]
