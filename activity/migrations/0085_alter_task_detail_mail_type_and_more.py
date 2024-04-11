# Generated by Django 4.2.6 on 2024-03-22 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0084_alter_task_detail_doc_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Personal', 'Personal'), ('Court', 'Court'), ('IPO', 'IPO'), ('Email', 'Email'), ('Mail', 'Mail')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='tran_type',
            field=models.CharField(blank=True, choices=[('Billable', 'Billable'), ('Non-Billable', 'Non-Billable')], max_length=15, null=True),
        ),
    ]
