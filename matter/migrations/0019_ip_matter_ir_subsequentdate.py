# Generated by Django 4.2.6 on 2024-02-29 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matter', '0018_alter_matters_folder'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip_matter',
            name='IR_subsequentDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
