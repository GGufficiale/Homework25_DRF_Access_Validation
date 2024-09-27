from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from celery import shared_task

from courses_lessons.models import Subscription


@shared_task
def send_email(course_id):
    """
    Отправляет письмо с уведомлением об изменении курса.
    """
    subs = Subscription.objects.filter(course=course_id, status=True)
    for sub in subs:
        course = sub.course
        user = sub.owner
        send_mail(
            subject=f'{course} обновился',
            message=f'{course} обновился',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False
        )
        print(f'Письмо отправлено пользователю {user.email}')