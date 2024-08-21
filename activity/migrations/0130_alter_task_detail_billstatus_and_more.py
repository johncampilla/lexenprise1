# Generated by Django 4.2.6 on 2024-07-26 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0129_alter_task_detail_billstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='billstatus',
            field=models.CharField(blank=True, choices=[('Unbilled', 'Unbilled'), ('Billed', 'Billed')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Mail', 'Mail'), ('Personal', 'Personal'), ('IPO', 'IPO'), ('Court', 'Court'), ('Email', 'Email')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='tran_type',
            field=models.CharField(blank=True, choices=[('Billable', 'Billable'), ('Non-Billable', 'Non-Billable')], max_length=15, null=True),
        ),
    ]
