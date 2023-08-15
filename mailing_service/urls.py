from django.contrib import admin
from django.urls import path, include

from mailing_service.apps import MailingServiceConfig
from mailing_service.views import index, MessageSenderCreateView, MessageSenderListView, MessageSenderDetailView, \
    MessageSenderUpdateView, MessageSenderDeleteView, CustomerCreateView, CustomerListView, CustomerDetailView, \
    CustomerUpdateView, CustomerDeleteView, AttemptListView, AttemptDetailView, AttemptDeleteView

app_name = MailingServiceConfig.name


urlpatterns = [
    path('', index),

    path('customer/create', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/list', CustomerListView. as_view(), name='customer_list'),
    path('customer/detail/<int:pk>', CustomerDetailView. as_view(), name='customer_detail'),
    path('customer/update/<int:pk>', CustomerUpdateView. as_view(), name='customer_update'),
    path('customer/delete/<int:pk>', CustomerDeleteView. as_view(), name='customer_delete'),


    path('sender/create', MessageSenderCreateView.as_view(), name='create'),
    path('sender/list', MessageSenderListView. as_view(), name='list'),
    path('sender/detail/<int:pk>', MessageSenderDetailView. as_view(), name='detail'),
    path('sender/update/<int:pk>', MessageSenderUpdateView. as_view(), name='update'),
    path('sender/delete/<int:pk>', MessageSenderDeleteView. as_view(), name='delete'),

    path('attempt/list', AttemptListView. as_view(), name='attempt_list'),
    path('attempt/detail/<int:pk>', AttemptDetailView. as_view(), name='attempt_detail'),
    path('attempt/delete/<int:pk>', AttemptDeleteView. as_view(), name='attempt_delete'),

]