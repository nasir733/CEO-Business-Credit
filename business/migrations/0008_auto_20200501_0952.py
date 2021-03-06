# Generated by Django 3.0.5 on 2020-05-01 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0007_auto_20200501_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storecreditvendorlist',
            name='apr',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='storecreditvendorlist',
            name='business_revenue',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='storecreditvendorlist',
            name='lender_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='storecreditvendorlist',
            name='personal_credit_score',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='storecreditvendorlist',
            name='strategy',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='storecreditvendorlist',
            name='term_length',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='storecreditvendorlist',
            name='time_in_business',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterModelTable(
            name='storecreditvendorlist',
            table='store_credit_vendor_2',
        ),
    ]
