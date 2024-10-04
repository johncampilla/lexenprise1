# Generated by Django 4.2.6 on 2024-07-23 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataconversion', '0017_csv_appstat'),
    ]

    operations = [
        migrations.CreateModel(
            name='csv_officers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CaseOfficers', models.CharField(blank=True, max_length=10, null=True)),
                ('OfficerName', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]