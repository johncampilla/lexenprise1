# Generated by Django 4.2.6 on 2024-07-23 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataconversion', '0020_csv_applicant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csv_applicant',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='csv_applicant',
            name='Class',
        ),
        migrations.RemoveField(
            model_name='csv_applicant',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='csv_applicant',
            name='Fax',
        ),
        migrations.RemoveField(
            model_name='csv_applicant',
            name='Nationality',
        ),
        migrations.RemoveField(
            model_name='csv_applicant',
            name='Telephone',
        ),
    ]
