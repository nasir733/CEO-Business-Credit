# Generated by Django 3.1.4 on 2021-01-21 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financing_portal', '0002_auto_20201217_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='recurring',
            field=models.CharField(choices=[('month', 'month'), ('year', 'year')], default=('month', 'month'), max_length=400),
        ),
    ]
