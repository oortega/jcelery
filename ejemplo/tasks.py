from __future__ import absolute_import, unicode_literals
from celery import shared_task
from time import sleep

# El decorador shared_task sirve para crear tareas independientes a la app.

@shared_task
def generar_reporte(num_emails):
    #simulamos que tarda 10 segundos
    sleep(10)

    return 'El reporte se envio correctamente'