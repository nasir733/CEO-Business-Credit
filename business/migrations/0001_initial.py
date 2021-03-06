# Generated by Django 3.0.5 on 2020-04-21 10:17

import business.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20200420_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc_name', models.CharField(max_length=50)),
                ('min_credit_score', models.CharField(max_length=50)),
                ('credit_bureau', models.CharField(max_length=50)),
                ('debt_ratio', models.CharField(max_length=50)),
                ('bankruptcy', models.CharField(max_length=50)),
                ('credit_data', models.CharField(max_length=50)),
                ('apr', models.CharField(max_length=50)),
                ('misc_info', models.CharField(max_length=50)),
                ('url', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'business_credit_card',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='BusinessTermLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lender_name', models.CharField(max_length=50)),
                ('personal_credit_score', models.CharField(max_length=50)),
                ('time_in_business', models.CharField(max_length=50)),
                ('business_revenue', models.CharField(max_length=15)),
                ('term_length', models.CharField(max_length=10)),
                ('apr', models.CharField(max_length=10)),
                ('strategy', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'term_loan',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='EquipmentFinancing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lender_name', models.CharField(max_length=50)),
                ('personal_credit_score', models.CharField(max_length=50)),
                ('time_in_business', models.CharField(max_length=50)),
                ('business_revenue', models.CharField(max_length=15)),
                ('term_length', models.CharField(max_length=10)),
                ('apr', models.CharField(max_length=10)),
                ('strategy', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'equipment_financing',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='FinancingPlanRegularPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('report_to', models.CharField(max_length=50, null=True)),
                ('monthly_payment', models.CharField(max_length=15, null=True)),
                ('estimated_term', models.CharField(max_length=50, null=True)),
                ('estimated_amount', models.CharField(max_length=5, null=True)),
                ('payment_terms', models.CharField(max_length=50, null=True)),
                ('terms', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'financingplanregularperson',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'industry',
            },
        ),
        migrations.CreateModel(
            name='InvoiceFactoring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lender_name', models.CharField(max_length=50)),
                ('personal_credit_score', models.CharField(max_length=50)),
                ('time_in_business', models.CharField(max_length=50)),
                ('business_revenue', models.CharField(max_length=15)),
                ('term_length', models.CharField(max_length=10)),
                ('apr', models.CharField(max_length=10)),
                ('strategy', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'invoice_factoring',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='InvoiceFinancing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lender_name', models.CharField(max_length=50)),
                ('personal_credit_score', models.CharField(max_length=50)),
                ('time_in_business', models.CharField(max_length=50)),
                ('business_revenue', models.CharField(max_length=15)),
                ('term_length', models.CharField(max_length=10)),
                ('apr', models.CharField(max_length=10)),
                ('strategy', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'invoice_financing',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='LinesOfCredit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lender_name', models.CharField(max_length=50)),
                ('personal_credit_score', models.CharField(max_length=50)),
                ('time_in_business', models.CharField(max_length=50)),
                ('business_revenue', models.CharField(max_length=15)),
                ('term_length', models.CharField(max_length=10)),
                ('apr', models.CharField(max_length=10)),
                ('strategy', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lines_of_credit',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PersonalCreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc_name', models.CharField(max_length=50)),
                ('min_credit_score', models.CharField(max_length=50)),
                ('credit_bureau', models.CharField(max_length=50)),
                ('debt_ratio', models.CharField(max_length=50)),
                ('bankruptcy', models.CharField(max_length=50)),
                ('credit_data', models.CharField(max_length=50)),
                ('apr', models.CharField(max_length=50)),
                ('misc_info', models.CharField(max_length=50)),
                ('url', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'personal_credit_card',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PersonalCreditTradeLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lender_name', models.CharField(max_length=50)),
                ('hard_check', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('strategy', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'personal_credit_tradeline',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PersonalLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lender_name', models.CharField(max_length=50)),
                ('terms', models.CharField(max_length=50)),
                ('inquiries', models.CharField(max_length=50)),
                ('credit_bureau', models.CharField(max_length=50)),
                ('states', models.CharField(max_length=50)),
                ('credit_score', models.CharField(max_length=50)),
                ('emp_length', models.CharField(max_length=50)),
                ('credit_history', models.CharField(max_length=50)),
                ('url', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'personal_loan',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SbaLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lender_name', models.CharField(max_length=50)),
                ('personal_credit_score', models.CharField(max_length=50)),
                ('time_in_business', models.CharField(max_length=50)),
                ('business_revenue', models.CharField(max_length=15)),
                ('term_length', models.CharField(max_length=10)),
                ('apr', models.CharField(max_length=10)),
                ('strategy', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sba_loan',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ShortTermLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lender_name', models.CharField(max_length=50)),
                ('personal_credit_score', models.CharField(max_length=50)),
                ('time_in_business', models.CharField(max_length=50)),
                ('business_revenue', models.CharField(max_length=15)),
                ('term_length', models.CharField(max_length=10)),
                ('apr', models.CharField(max_length=10)),
                ('strategy', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'short_term_loan',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='WebsiteCreation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry_name', models.CharField(max_length=50)),
                ('booking_on_page', models.CharField(max_length=50)),
                ('business_name', models.CharField(max_length=50)),
                ('chat_bot', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('theme', models.CharField(max_length=50)),
                ('pages_needed', models.CharField(max_length=50)),
                ('services', models.CharField(max_length=50)),
                ('domain', models.CharField(max_length=50)),
                ('about_you', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=200)),
                ('domain_owned', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'website_creation',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TollFreeNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toll_free_number_needed', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
            ],
            options={
                'db_table': 'toll_free_number',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StoreCreditVendorList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('terms', models.CharField(max_length=50)),
                ('report_to', models.CharField(max_length=50)),
                ('url', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Category')),
            ],
            options={
                'db_table': 'store_credit_vendor',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StarterVendorList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('terms', models.CharField(max_length=50)),
                ('report_to', models.CharField(max_length=50)),
                ('url', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Category')),
            ],
            options={
                'db_table': 'starter_vendor_list',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RevolvingCredit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('terms', models.CharField(max_length=50)),
                ('report_to', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Category')),
            ],
            options={
                'db_table': 'revolving_credit',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RevolvingBusinessCreditVendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('terms', models.CharField(max_length=50)),
                ('report_to', models.CharField(max_length=50)),
                ('url', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Category')),
            ],
            options={
                'db_table': 'revolving_business_credit',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RevenueLending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fico_score', models.CharField(max_length=50)),
                ('equifax_score', models.CharField(max_length=50)),
                ('transunion_score', models.CharField(max_length=50)),
                ('avg_monthly_revenue', models.CharField(max_length=50)),
                ('abg_daily_balance', models.CharField(max_length=50)),
                ('avg_monthly_ending_balance', models.CharField(max_length=50)),
                ('business_debt', models.CharField(max_length=50)),
                ('liens', models.CharField(max_length=50)),
                ('business_bank_account', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('registered_at', models.DateTimeField(blank=True, null=True)),
                ('lender_name', models.CharField(max_length=50)),
                ('personal_credit_score', models.CharField(max_length=50)),
                ('time_in_business', models.CharField(max_length=50)),
                ('business_revenue', models.CharField(max_length=50)),
                ('term_length', models.CharField(max_length=50)),
                ('apr', models.CharField(max_length=50)),
                ('strategy', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Industry')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
            ],
            options={
                'db_table': 'revenue_lending',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_creation', models.CharField(max_length=50)),
                ('dns_number', models.CharField(max_length=50)),
                ('virtual_number', models.CharField(max_length=50)),
                ('fax_number', models.CharField(max_length=50)),
                ('toll_free_number', models.CharField(max_length=50)),
                ('business_bank_account', models.CharField(max_length=50)),
                ('listing', models.CharField(max_length=50)),
                ('professional_email_address', models.CharField(max_length=50)),
                ('domain', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
            ],
            options={
                'db_table': 'progress',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProfessionalEmailAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address_needed', models.CharField(max_length=50)),
                ('domain_present', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
            ],
            options={
                'db_table': 'professional_email_address',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Nopg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('report_to', models.CharField(max_length=50)),
                ('monthly_payment', models.CharField(max_length=15)),
                ('estimated_term', models.DateField()),
                ('payment_terms', models.CharField(max_length=50)),
                ('url', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Category')),
            ],
            options={
                'db_table': 'nopg',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Lender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('report_to', models.CharField(max_length=50, null=True)),
                ('monthly_payment', models.CharField(max_length=15, null=True)),
                ('estimated_term', models.CharField(max_length=50, null=True)),
                ('estimated_amount', models.CharField(max_length=5, null=True)),
                ('payment_terms', models.CharField(max_length=50, null=True)),
                ('terms', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.Category')),
            ],
            options={
                'db_table': 'lender',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Fax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fax_needed', models.CharField(max_length=50)),
                ('created_at', models.CharField(max_length=50)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
            ],
            options={
                'db_table': 'fax',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=50)),
                ('domain_needed', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
            ],
            options={
                'db_table': 'domain',
            },
            bases=(business.models.ModelMixin, models.Model),
        ),
    ]
