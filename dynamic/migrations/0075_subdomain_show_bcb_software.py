# Generated by Django 3.2.5 on 2021-08-06 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0074_auto_20210805_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdomain',
            name='show_bcb_software',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
