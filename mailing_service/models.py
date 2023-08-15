from datetime import date, datetime

from django.db import models

from users.models import User


class Customer(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование клиента')
    email = models.EmailField(unique=True, verbose_name='Адрес электронной почты')
    description = models.TextField(verbose_name='Описание клиента', blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Создатель записи')
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class MessageSender(models.Model):

    FREQUENCY = [
        ('ONCE', 'Один раз'),
        ('DAILY', '1 раз в день'),
        ('WEEKLY', '1 раз в неделю'),
        ('MONTHLY', '1 раз в месяц'),
    ]
    STATUS = [
        ('CREATED', 'Создана'),
        ('COMPLETED', 'Завершена'),
        ('LAUNCHED', 'Запущена'),
    ]

    # Message
    subject = models.CharField(max_length=254, verbose_name='Тема')
    body = models.TextField(verbose_name='Сообщение')
    # Sending
    start_date = models.DateField(default=date.today, verbose_name='Дата начала')
    # next_time = models.TimeField(default=datetime.now, verbose_name='Время рассылки')
    end_date = models.DateField(default=date.today, verbose_name='Дата окончания')
    frequency = models.CharField(max_length=7, choices=FREQUENCY, default='ONCE', verbose_name='Периодичность рассылки')
    status = models.CharField(max_length=50, default='CREATED', choices=STATUS, verbose_name='Статус')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Создатель рассылки')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Рассылка сообщения'
        verbose_name_plural = 'Рассылки сообщений'


class Attempt(models.Model):
    STATUS = [
        ('DELIVERED', 'доставлено'),
        ('NOT_DELIVERED', 'не доставлено'),
    ]

    message_sender = models.ForeignKey(MessageSender, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время рассылки сообщения')
    status = models.CharField(max_length=13, choices=STATUS, verbose_name='Статус попытки')
    response = models.TextField(blank=True, verbose_name='Ответ сервера')

    def __str__(self):
        return f"{self.message_sender.subject} - {self.customer} - {self.created_at}"

    class Meta:
        verbose_name = 'Статистика (попытка)'
        verbose_name_plural = 'Статистики (попытки)'

