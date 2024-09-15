from django.contrib.auth.models import AbstractUser
from django.db import models

from courses_lessons.models import Lesson, Course

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта', help_text='Укажите почту')
    phone = models.CharField(max_length=35, verbose_name='Телефон', help_text='Введите телефон', **NULLABLE)
    city = models.CharField(max_length=35, verbose_name='Город', help_text='Введите ваш город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='Аватар', help_text='Загрузите свое фото',
                               **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [('cash', 'наличные'), ('card', 'банковский перевод')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь',
                             help_text='Выберите пользователя')
    payment_date = models.DateField(auto_now=True, verbose_name='дата оплаты', help_text='Введите дату оплаты',
                                    **NULLABLE)
    course_paid = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс',
                                    help_text='Выберите оплаченный курс', **NULLABLE)
    lesson_paid = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок',
                                    help_text='Выберите оплаченный урок', **NULLABLE)
    payment_method = models.CharField(max_length=35, choices=PAYMENT_METHOD_CHOICES, default='card',
                                      verbose_name='Способ оплаты', help_text='выберите способ оплаты', **NULLABLE)
    amount = models.PositiveIntegerField(verbose_name='Сумма оплаты', help_text='укажите сумму оплаты', **NULLABLE)
    session_id = models.CharField(max_length=255, verbose_name='ID сессии', help_text='укажите ID сессии', **NULLABLE)
    link = models.URLField(max_length=400, verbose_name='Ссылка на оплату', help_text='укажите ссылку на оплату',
                           **NULLABLE)

    def __str__(self):
        return (f'{self.user}: {self.payment_date}, {self.course_paid if self.course_paid else self.lesson_paid}, '
                f'{self.amount}')

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
