# Generated by Django 4.2.6 on 2024-03-19 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataconversion', '0002_egazette'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egazette',
            name='Applicant',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='egazette',
            name='Mark',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='egazette',
            name='Nice_class',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]