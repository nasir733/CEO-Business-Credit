# Generated by Django 3.0.5 on 2020-05-01 09:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0004_virtualcard_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='virtualcard',
            name='name',
        ),
    ]
