# Generated by Django 4.2.6 on 2024-07-23 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataconversion', '0018_csv_officers'),
    ]

    operations = [
        migrations.CreateModel(
            name='csv_docs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DocumentType', models.CharField(blank=True, max_length=10)),
                ('Description', models.CharField(max_length=100)),
            ],
        ),
    ]
