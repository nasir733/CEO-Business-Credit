# Generated by Django 3.1.1 on 2020-11-19 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0066_auto_20201109_1032'),
        ('dynamic', '0043_auto_20201119_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdomain',
            name='admins',
            field=models.ManyToManyField(null=True, related_name='portals', to='user.Profile'),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='androidApp',
            field=models.URLField(default='https://play.google.com/store/apps/details?id=com.millennialbusinessbuilders.businesscreditbuilders', max_length=300),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='chromeExt',
            field=models.URLField(default='https://chrome.google.com/webstore/detail/the-business-credit-build/jpbbaabmhfpfdjnomgdieempedlaelfi', max_length=300),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='iphoneApp',
            field=models.URLField(default='https://apps.apple.com/us/app/the-business-credit-builders/id1528895728', max_length=300),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='is_payment_done',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='subdomain',
            name='webinar',
            field=models.URLField(default='https://youtu.be/xNCfnbGT5hY', max_length=300),
        ),
    ]
