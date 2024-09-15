# Generated by Django 5.1 on 2024-09-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.PositiveIntegerField(blank=True, help_text='укажите сумму оплаты', null=True, verbose_name='Сумма оплаты'),
        ),
        migrations.AddField(
            model_name='payment',
            name='link',
            field=models.URLField(blank=True, help_text='укажите ссылку на оплату', max_length=400, null=True, verbose_name='Ссылка на оплату'),
        ),
        migrations.AddField(
            model_name='payment',
            name='session_id',
            field=models.CharField(blank=True, help_text='укажите ID сессии', max_length=255, null=True, verbose_name='ID сессии'),
        ),
    ]
