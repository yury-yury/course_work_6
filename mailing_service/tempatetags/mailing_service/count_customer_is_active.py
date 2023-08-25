from django import template

from mailing_service.models import Customer


register = template.Library()


@register.simple_tag
def count_customer_is_active():
    count = Customer.objects.filter(is_active=True).count()
    return f'{count}'