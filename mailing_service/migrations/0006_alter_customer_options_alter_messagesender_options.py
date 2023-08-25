# Generated by Django 4.2.3 on 2023-08-25 16:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mailing_service", "0005_alter_customer_email"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customer",
            options={
                "permissions": [("set_active_customer", "Can set active customer")],
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
            },
        ),
        migrations.AlterModelOptions(
            name="messagesender",
            options={
                "permissions": [
                    ("set_messagesender_status", "Can set messagesender status")
                ],
                "verbose_name": "Рассылка сообщения",
                "verbose_name_plural": "Рассылки сообщений",
            },
        ),
    ]