# Generated by Django 3.1.1 on 2021-02-28 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0071_auto_20210228_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='can_see_only_created_portals',
            field=models.BooleanField(default=False),
        ),
    ]
