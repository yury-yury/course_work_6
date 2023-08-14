# Generated by Django 4.2.3 on 2023-08-12 21:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="MessageSender",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=254, verbose_name="Тема")),
                ("body", models.TextField(verbose_name="Сообщение")),
                (
                    "start_date",
                    models.DateField(
                        default=datetime.date.today, verbose_name="Дата начала"
                    ),
                ),
                (
                    "next_time",
                    models.TimeField(
                        default=datetime.datetime.now, verbose_name="Время рассылки"
                    ),
                ),
                (
                    "end_date",
                    models.DateField(
                        default=datetime.date.today, verbose_name="Дата окончания"
                    ),
                ),
                (
                    "frequency",
                    models.CharField(
                        choices=[
                            ("ONCE", "Один раз"),
                            ("DAILY", "1 раз в день"),
                            ("WEEKLY", "1 раз в неделю"),
                            ("MONTHLY", "1 раз в месяц"),
                        ],
                        max_length=7,
                        verbose_name="Периодичность рассылки",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("CREATED", "Создана"),
                            ("COMPLETED", "Завершена"),
                            ("LAUNCHED", "Запущена"),
                        ],
                        default="CREATED",
                        max_length=50,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Создатель рассылки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка сообщения",
                "verbose_name_plural": "Рассылки сообщений",
            },
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=150, verbose_name="Наименование клиента"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, verbose_name="Адрес электронной почты"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Описание клиента"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Активный"),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Создатель записи",
                    ),
                ),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
            },
        ),
        migrations.CreateModel(
            name="Attempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время рассылки сообщения"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("DELIVERED", "доставлено"),
                            ("NOT_DELIVERED", "не доставлено"),
                        ],
                        max_length=13,
                        verbose_name="Статус попытки",
                    ),
                ),
                (
                    "response",
                    models.TextField(blank=True, verbose_name="Ответ сервера"),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailing_service.customer",
                    ),
                ),
                (
                    "message_sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailing_service.messagesender",
                    ),
                ),
            ],
            options={
                "verbose_name": "Статистика (попытка)",
                "verbose_name_plural": "Статистики (попытки)",
            },
        ),
    ]
