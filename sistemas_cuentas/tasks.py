from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

#@shared_task
#def enviar_alarma(correo, mensaje):
#    send_mail(
#        'Alarma de informe',
#        mensaje,
#        settings.DEFAULT_FROM_EMAIL,
#        [correo],
#        fail_silently=False,
#        
#    )
@shared_task
def prueba():
    current_time = timezone.now()
    print(f"La hora actual es: {current_time}")