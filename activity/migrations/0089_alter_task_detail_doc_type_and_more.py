# Generated by Django 4.2.6 on 2024-03-22 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0088_alter_task_detail_billstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='doc_type',
            field=models.CharField(blank=True, choices=[('Outgoing', 'Outgoing'), ('Others', 'Others'), ('Incoming', 'Incoming')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('IPO', 'IPO'), ('Email', 'Email'), ('Mail', 'Mail'), ('Personal', 'Personal'), ('Court', 'Court')], max_length=15, null=True),
        ),
    ]
