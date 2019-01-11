from django.conf.urls import url
from django.contrib import admin
from ejemplo import views

urlpatterns = [
 
   # url que ejecuta la tarea.
    url(r'^generar_reporte$', views.generar_reporte)
]