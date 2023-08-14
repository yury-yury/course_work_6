from django.contrib import admin

from mailing_service.models import Customer, MessageSender, Attempt

admin.site.register(Customer)
admin.site.register(MessageSender)
admin.site.register(Attempt)
