# Generated by Django 4.2.6 on 2024-07-26 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0017_alter_client_data_client_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client_data',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
