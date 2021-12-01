# Generated by Django 3.1.4 on 2021-01-22 00:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0049_auto_20201208_1800'),
        ('business', '0049_auto_20210122_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='NonReportingTradeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Product', max_length=500, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=100, validators=[django.core.validators.MinValueValidator(0)])),
                ('charge', models.DecimalField(decimal_places=2, default=0, max_digits=100, validators=[django.core.validators.MinValueValidator(0)])),
                ('recurring', models.IntegerField(choices=[(1, 'One time'), (2, 'Month'), (3, 'Year')], default=1, null=True)),
                ('product_id', models.CharField(blank=True, max_length=100, null=True)),
                ('price_id', models.CharField(blank=True, max_length=100, null=True)),
                ('price_lookup', models.CharField(blank=True, max_length=100, null=True)),
                ('company_name', models.CharField(max_length=500, null=True)),
                ('product', models.CharField(max_length=500, null=True)),
                ('tradeline_amount', models.CharField(max_length=500, null=True)),
                ('tradeline_credit_amount', models.CharField(max_length=500, null=True)),
                ('company_reports_to', models.CharField(max_length=500, null=True)),
                ('we_can_help', models.BooleanField(default=True, null=True)),
                ('recommended', models.TextField(blank=True, null=True)),
                ('tier', models.CharField(blank=True, max_length=10, null=True)),
                ('terms', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('website_link', models.URLField(blank=True, null=True)),
                ('whitelabel_portal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dynamic.subdomain')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
