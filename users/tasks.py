import datetime
from celery import shared_task
from users.models import User
from dateutil.relativedelta import relativedelta
from django.utils import timezone


@shared_task
def check_user_activity():
    """
    Проверяем активность пользователя, если больше 30 дней, деактивируем
    """
    now = timezone.now()
    month_ago = now - relativedelta(months=1)
    qs = User.objects.filter(last_login__lt=month_ago, is_active=True)
    qs.update(is_active=False)
