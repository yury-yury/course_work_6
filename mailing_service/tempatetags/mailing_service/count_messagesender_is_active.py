from django import template

from mailing_service.models import MessageSender

register = template.Library()


@register.simple_tag
def count_messagesender_is_active():
    count = MessageSender.objects.filter(status__in=['CREATED', 'LAUNCHED']).count()
    return f'{count}'