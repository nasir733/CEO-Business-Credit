# Generated by Django 3.1.1 on 2020-11-09 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0032_subdomain_show_credit_repair_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdomain',
            name='show_why_buy_from_us',
            field=models.BooleanField(default=True),
        ),
    ]
