# Generated by Django 4.2.6 on 2024-07-14 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0108_alter_task_detail_billstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Email', 'Email'), ('Mail', 'Mail'), ('Court', 'Court'), ('IPO', 'IPO'), ('Personal', 'Personal')], max_length=15, null=True),
        ),
    ]