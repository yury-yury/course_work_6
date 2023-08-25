from django import template

from mailing_service.models import MessageSender

register = template.Library()


@register.simple_tag
def count_messagesender():
    count = MessageSender.objects.all().count()
    return f'{count}'