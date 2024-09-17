import requests
import stripe
from forex_python.converter import CurrencyRates
from rest_framework import status

from config import settings
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):
    """Создаем stripe продукт"""
    title_product = f'{instance.course_paid}' if instance.course_paid else f'{instance.lesson_paid}'
    stripe_product = stripe.Product.create(name=f"{title_product}")
    return stripe_product.get('id')


# def convert_rub_to_usd(amount):
#     """Метод конвертации рублей в доллары"""
#     c = CurrencyRates()
#     rate = c.get_rate('RUB', 'USD')
#     return int(amount * rate)

def convert_currencies(rub_price):
    """Метод конвертации курса доллара к рублю"""
    rub_price = 0
    response = requests.get(
        f'{settings.CURRENCY_API_URL}v3/latest?apikey={settings.CURRENCY_API_KEY}&currencies=USD'
    )
    if response.status_code == status.HTTP_200_OK:
        usd_rate = response.json()['data']['USD']['value']
        rub_price = rub_price * usd_rate
    return rub_price


def create_stripe_price(amount):
    """Метод создания цены в Stripe"""
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,  # умножаем из-за копеек
        product_data={"name": "Payment"},
    )


def create_stripe_session(price):
    """Создает сессию на оплату в страйпе"""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",  # здесь можно создать ссылку на шаблон с благодарностями юзеру за оплату
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')
