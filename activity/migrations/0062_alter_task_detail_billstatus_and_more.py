# Generated by Django 4.2.6 on 2024-03-05 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0061_alter_task_detail_billstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='billstatus',
            field=models.CharField(blank=True, choices=[('Billed', 'Billed'), ('Unbilled', 'Unbilled')], default='Unbilled', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='doc_type',
            field=models.CharField(blank=True, choices=[('Others', 'Others'), ('Outgoing', 'Outgoing'), ('Incoming', 'Incoming')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Email', 'Email'), ('Personal', 'Personal'), ('IPO', 'IPO'), ('Court', 'Court'), ('Mail', 'Mail')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='tran_type',
            field=models.CharField(blank=True, choices=[('Billable', 'Billable'), ('Non-Billable', 'Non-Billable')], max_length=15, null=True),
        ),
    ]
