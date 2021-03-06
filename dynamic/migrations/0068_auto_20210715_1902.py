# Generated by Django 3.2.5 on 2021-07-15 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0067_auto_20210715_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdomain',
            name='navigation_bar_link_1_link',
            field=models.CharField(default='/', max_length=200),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='navigation_bar_link_1_text',
            field=models.CharField(default='Home', help_text='add the text that you want to show in the first link in the navbar', max_length=200),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='navigation_bar_link_2_Link',
            field=models.CharField(default='/about-us', help_text='add the link that you want to show on the navbar', max_length=200),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='navigation_bar_link_2_text',
            field=models.CharField(default='AboutUs', help_text='add the text that you want to show in the first link in the navbar', max_length=200),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='navigation_bar_link_3_Link',
            field=models.CharField(default='/pricing', help_text='add the link that you want to show on the navbar', max_length=200),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='navigation_bar_link_3_text',
            field=models.CharField(default='Pricing', help_text='add the text that you want to show in the first link in the navbar', max_length=200),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='navigation_bar_link_4_Link',
            field=models.CharField(default='/services', help_text='add the link that you want to show on the navbar', max_length=200),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='navigation_bar_link_4_text',
            field=models.CharField(default='Services', help_text='add the text that you want to show in the first link in the navbar', max_length=200),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='navigation_bar_link_5_Link',
            field=models.CharField(default='/whitelabel', help_text='add the link that you want to show on the navbar', max_length=200),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='navigation_bar_link_5_text',
            field=models.CharField(default='White Label Program', help_text='add the text that you want to show in the first link in the navbar', max_length=200),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='navigation_bar_link_6_Link',
            field=models.CharField(default='/dashboard', help_text='add the link that you want to show on the navbar', max_length=200),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='navigation_bar_link_6_text',
            field=models.CharField(default='Client Login', help_text='add the text that you want to show in the first link in the navbar', max_length=200),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='show_navigation_bar_link_1',
            field=models.BooleanField(default=True, help_text='check the box if you want to show the navbar links'),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='show_navigation_bar_link_2',
            field=models.BooleanField(default=True, help_text='check the box if you want to show the navbar links'),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='show_navigation_bar_link_3',
            field=models.BooleanField(default=True, help_text='check the box if you want to show the navbar links'),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='show_navigation_bar_link_4',
            field=models.BooleanField(default=True, help_text='check the box if you want to show the navbar links'),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='show_navigation_bar_link_5',
            field=models.BooleanField(default=True, help_text='check the box if you want to show the navbar links'),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='show_navigation_bar_link_6',
            field=models.BooleanField(default=True, help_text='check the box if you want to show the navbar links'),
        ),
        migrations.AddField(
            model_name='subdomain',
            name='show_navigation_bar_links',
            field=models.BooleanField(default=True, help_text='check the box if you want to show the navbar links'),
        ),
    ]
