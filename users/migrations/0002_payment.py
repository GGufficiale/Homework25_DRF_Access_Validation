# Generated by Django 5.1 on 2024-09-02 17:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_lessons', '0002_rename_lesson_lesson_course'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(auto_now=True, help_text='Введите дату оплаты', null=True, verbose_name='дата оплаты')),
                ('payment_method', models.CharField(blank=True, choices=[('cash', 'наличные'), ('card', 'банковский перевод')], default='card', help_text='выберите способ оплаты', max_length=35, null=True, verbose_name='Способ оплаты')),
                ('course_paid', models.ForeignKey(blank=True, help_text='Выберите оплаченный курс', null=True, on_delete=django.db.models.deletion.CASCADE, to='courses_lessons.course', verbose_name='оплаченный курс')),
                ('lesson_paid', models.ForeignKey(blank=True, help_text='Выберите оплаченный урок', null=True, on_delete=django.db.models.deletion.CASCADE, to='courses_lessons.lesson', verbose_name='оплаченный урок')),
                ('user', models.ForeignKey(help_text='Выберите пользователя', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'платеж',
                'verbose_name_plural': 'платежи',
            },
        ),
    ]
