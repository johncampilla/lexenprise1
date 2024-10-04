# Generated by Django 4.2.6 on 2024-07-23 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataconversion', '0019_csv_docs'),
    ]

    operations = [
        migrations.CreateModel(
            name='csv_applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ApplicantCode', models.CharField(blank=True, max_length=200)),
                ('ApplicantName', models.CharField(blank=True, max_length=200)),
                ('Class', models.CharField(blank=True, max_length=20)),
                ('Address', models.CharField(blank=True, max_length=20)),
                ('Nationality', models.CharField(blank=True, max_length=20)),
                ('Fax', models.CharField(blank=True, max_length=20)),
                ('Email', models.CharField(blank=True, max_length=20)),
                ('Telephone', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]