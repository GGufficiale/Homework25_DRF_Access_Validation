from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from celery import shared_task

from courses_lessons.models import Subscription, Course


@shared_task
def send_email(course_id):
    """
    Отправляет письмо с уведомлением об изменении курса.
    """
    course = Course.objects.get(id=course_id)

    subs = Subscription.objects.filter(course=course_id, status=True)
    emails = subs.values_list('user__email', flat=True)

    send_mail(
        subject=f'{course.title} обновился',
        message=f'{course.title} обновился',
        from_email=EMAIL_HOST_USER,
        recipient_list=emails,
        fail_silently=False
    )