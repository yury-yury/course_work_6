# Generated by Django 4.2.3 on 2023-08-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mailing_service", "0003_alter_customer_creator_alter_messagesender_creator"),
    ]

    operations = [
        migrations.AlterField(
            model_name="messagesender",
            name="frequency",
            field=models.CharField(
                choices=[
                    ("ONCE", "Один раз"),
                    ("DAILY", "1 раз в день"),
                    ("WEEKLY", "1 раз в неделю"),
                    ("MONTHLY", "1 раз в месяц"),
                ],
                default="ONCE",
                max_length=7,
                verbose_name="Периодичность рассылки",
            ),
        ),
    ]