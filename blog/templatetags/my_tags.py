from django import template

from mailing_service.models import Customer, MessageSender

register = template.Library()


@register.filter()
def mediapath(value) -> str:
    if value:
        return f'/media/{value}'
    return '/media/default.jpg'


@register.simple_tag()
def mediafile(value) -> str:
    if value:
        return f'/media/{value}'
    return '/media/default.jpg'


@register.simple_tag
def count_customer_is_active():
    count = Customer.objects.filter(is_active=True).count()
    return f'{count}'


@register.simple_tag
def count_messagesender_is_active():
    count = MessageSender.objects.filter(status__in=['CREATED', 'LAUNCHED']).count()
    return f'{count}'


@register.simple_tag
def count_messagesender():
    count = MessageSender.objects.all().count()
    return f'{count}'
