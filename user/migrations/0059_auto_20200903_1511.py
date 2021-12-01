# Generated by Django 3.1.1 on 2020-09-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0058_auto_20200903_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='client_email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='client_name',
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='whitelabel_portal',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
