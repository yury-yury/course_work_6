from django.contrib import admin
from django.urls import path, include

from mailing_service.apps import MailingServiceConfig
from mailing_service.views import index, MessageSenderCreateView, MessageSenderListView

app_name = MailingServiceConfig.name


urlpatterns = [
    path('', index),
    path('create', MessageSenderCreateView.as_view(), name='create'),
    path('list', MessageSenderListView. as_view(), name='list'),

]