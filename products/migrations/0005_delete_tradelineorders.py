# Generated by Django 3.0.5 on 2020-08-28 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_tradelines_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TradelineOrders',
        ),
    ]
