# Generated by Django 4.2.3 on 2023-08-13 11:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mailing_service", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="messagesender",
            name="next_time",
        ),
    ]
