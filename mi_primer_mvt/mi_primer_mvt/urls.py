from django.contrib import admin
from django.urls import path
from mi_primer_mvt.views import saludo, segundo_template, template_con_lista
from parientes.views import create_datos_familiares, list_parientes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name='saludo'),
    path('segundo_template/', segundo_template, name='segundo_template'),
    path('template_con_lista/', template_con_lista, name='template_con_lista'),
    path('create_datos_familiares/', create_datos_familiares, name='create_datos_familiares'),
    path('list_parientes/', list_parientes, name='list_parientes')
]
