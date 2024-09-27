from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_email(email, ):
    """
    Отправляет письмо с уведомлением об изменении курса.
    """
    send_mail(
        subject="Обновление",
        message="Курс по Вашей подписке обновлен",
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
    )
