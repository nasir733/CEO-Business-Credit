# Generated by Django 3.0.5 on 2020-08-29 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0016_merge_20200830_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdomain',
            name='accent_color',
            field=models.CharField(default='#1c6ef9', max_length=200),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='bg_color',
            field=models.CharField(default='#f2f2f2', max_length=200),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='primary_color',
            field=models.CharField(default='#115d22', max_length=200),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='secondary_color',
            field=models.CharField(default='#dee1e6', max_length=200),
        ),
    ]
