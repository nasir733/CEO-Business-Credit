# Generated by Django 3.1.1 on 2020-09-17 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0020_auto_20200905_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdomain',
            name='extensionVideo',
            field=models.URLField(default='http://youtube.com', max_length=300),
            preserve_default=False,
        ),
    ]
