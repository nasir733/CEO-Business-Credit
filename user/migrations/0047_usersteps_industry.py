# Generated by Django 3.0.5 on 2020-07-19 17:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0046_auto_20200712_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersteps',
            name='industry',
            field=models.IntegerField(
                choices=[(1, 'Electrician'), (2, 'Gardener'), (3, 'Tattoo Artist'), (4, 'Photography'),
                         (5, 'Limo Service'), (6, 'Nutrition Advisor'), (7, 'Life Coach'), (8, 'Veterinary clinic'),
                         (9, 'Laundromat'), (10, 'Fitness Club'), (11, 'Dentist'), (12, 'Consulting'),
                         (13, 'Auto Repair'), (14, 'Tutor'), (15, 'Bakery'), (16, 'Financial Advisor'), (17, 'Lawyer'),
                         (18, 'Marketing Agency'), (19, 'Trucking'), (20, 'Locksmith'), (21, 'Medical Clinic'),
                         (22, 'Dance Studio'), (23, 'Carpenter'), (24, 'Moving Company'), (25, 'Hair Salon'),
                         (26, 'Cleaning Service'), (27, 'Car Dealer'), (28, 'Portfolio'), (29, 'Real Estate'),
                         (30, 'Preschool'), (31, 'Spa Service'), (32, 'Physical Therapist')], default=1, null=True,
                verbose_name='Industry'),
        ),
    ]
