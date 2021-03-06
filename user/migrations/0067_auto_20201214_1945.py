# Generated by Django 3.1.1 on 2020-12-14 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0066_auto_20201109_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='available_credit_limit',
            field=models.DecimalField(decimal_places=2, default=1500, max_digits=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='credit_line',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=100),
        ),
    ]
