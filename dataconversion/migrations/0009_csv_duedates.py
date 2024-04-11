# Generated by Django 4.2.6 on 2024-03-20 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataconversion', '0008_csv_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='csv_duedates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClientNo', models.CharField(blank=True, max_length=15, null=True)),
                ('ApplicationNo', models.CharField(blank=True, max_length=25, null=True)),
                ('DueDates', models.DateField(blank=True, null=True)),
                ('DueCode', models.CharField(blank=True, max_length=15, null=True)),
                ('Activities', models.TextField(blank=True, null=True)),
                ('ReferenceNumber', models.CharField(blank=True, max_length=60, null=True)),
                ('Done', models.CharField(blank=True, max_length=5, null=True)),
                ('ActionDate', models.DateField(blank=True, null=True)),
                ('Complied', models.CharField(blank=True, max_length=5, null=True)),
                ('DateComplied', models.DateField(blank=True, null=True)),
                ('Remarks', models.TextField(blank=True, null=True)),
            ],
        ),
    ]