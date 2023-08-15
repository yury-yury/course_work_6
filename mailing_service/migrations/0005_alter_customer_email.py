# Generated by Django 4.2.3 on 2023-08-15 15:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mailing_service", "0004_alter_messagesender_frequency"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="Адрес электронной почты"
            ),
        ),
    ]