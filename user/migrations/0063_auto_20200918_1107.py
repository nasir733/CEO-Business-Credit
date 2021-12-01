# Generated by Django 3.1.1 on 2020-09-18 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0062_auto_20200914_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='billing_city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Billing City'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='billing_country',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Billing Country'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='billing_phone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Billing Phone'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='billing_state',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Billing State'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='billing_street_address_1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Billing Address Line 1'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='billing_zip_code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Billing Zip Code'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='duns',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='DUNS Number'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='fax_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Fax Number'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='toll_free_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Toll Free Number'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='website',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Website'),
        ),
    ]