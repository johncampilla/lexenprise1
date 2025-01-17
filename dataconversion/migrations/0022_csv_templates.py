# Generated by Django 4.2.6 on 2024-07-23 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataconversion', '0021_remove_csv_applicant_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='csv_templates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DocumentCode', models.CharField(blank=True, max_length=20)),
                ('Description', models.CharField(blank=True, max_length=200)),
                ('WithEnclosure', models.CharField(blank=True, max_length=5)),
                ('ApplicationType', models.CharField(blank=True, max_length=10)),
                ('TaskCode', models.CharField(blank=True, max_length=10)),
                ('DocPath', models.CharField(blank=True, max_length=100)),
                ('Operation', models.CharField(blank=True, max_length=5)),
            ],
        ),
    ]
