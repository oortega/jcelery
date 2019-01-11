from django.http import HttpResponse
from .tasks import simulate_send_emails

# Vista que llama a la tarea.
def generar_reporte(request):
    generar_reporte.delay(10)
    
    return HttpResponse('En breve se enviara su reporte')