# Generated by Django 4.2.6 on 2023-12-01 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0015_alter_task_detail_billstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Mail', 'Mail'), ('Court', 'Court'), ('Personal', 'Personal'), ('IPO', 'IPO'), ('Email', 'Email')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='tran_type',
            field=models.CharField(blank=True, choices=[('Non-Billable', 'Non-Billable'), ('Billable', 'Billable')], max_length=15, null=True),
        ),
    ]
