# Generated by Django 3.0.5 on 2020-05-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20200501_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nopg',
            name='reports_to',
            field=models.CharField(max_length=200),
        ),
    ]