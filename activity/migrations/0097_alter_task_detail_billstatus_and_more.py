# Generated by Django 4.2.6 on 2024-03-27 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0096_alter_task_detail_billstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='billstatus',
            field=models.CharField(blank=True, choices=[('Billed', 'Billed'), ('Unbilled', 'Unbilled')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('IPO', 'IPO'), ('Mail', 'Mail'), ('Court', 'Court'), ('Personal', 'Personal'), ('Email', 'Email')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='tran_type',
            field=models.CharField(blank=True, choices=[('Non-Billable', 'Non-Billable'), ('Billable', 'Billable')], max_length=15, null=True),
        ),
    ]
