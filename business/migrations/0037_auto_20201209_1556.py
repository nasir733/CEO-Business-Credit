# Generated by Django 3.1.1 on 2020-12-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0036_customtier'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtier',
            name='tier',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='tier1',
            name='tier',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='tier2',
            name='tier',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='tier3',
            name='tier',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='tier4',
            name='tier',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customtier',
            name='company_name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customtier',
            name='company_reports_to',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customtier',
            name='product',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customtier',
            name='tradeline_amount',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customtier',
            name='tradeline_credit_amount',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier1',
            name='company_name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier1',
            name='company_reports_to',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier1',
            name='product',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier1',
            name='tradeline_amount',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier1',
            name='tradeline_credit_amount',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier2',
            name='company_name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier2',
            name='company_reports_to',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier2',
            name='product',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier2',
            name='tradeline_amount',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier2',
            name='tradeline_credit_amount',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier3',
            name='company_name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier3',
            name='company_reports_to',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier3',
            name='product',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier3',
            name='tradeline_amount',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier3',
            name='tradeline_credit_amount',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier4',
            name='company_name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier4',
            name='company_reports_to',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier4',
            name='product',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier4',
            name='tradeline_amount',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tier4',
            name='tradeline_credit_amount',
            field=models.CharField(max_length=500, null=True),
        ),
    ]