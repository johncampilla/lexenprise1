# Generated by Django 4.2.6 on 2024-03-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataconversion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='egazette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Application_Number', models.CharField(blank=True, max_length=25, null=True)),
                ('Filing_Date', models.CharField(blank=True, max_length=40, null=True)),
                ('Mark', models.CharField(blank=True, max_length=60, null=True)),
                ('Applicant', models.CharField(blank=True, max_length=60, null=True)),
                ('Nice_class', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
    ]
