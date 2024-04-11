# Generated by Django 4.2.6 on 2024-03-22 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0090_alter_task_detail_billstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='doc_type',
            field=models.CharField(blank=True, choices=[('Incoming', 'Incoming'), ('Outgoing', 'Outgoing'), ('Others', 'Others')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('IPO', 'IPO'), ('Personal', 'Personal'), ('Email', 'Email'), ('Mail', 'Mail'), ('Court', 'Court')], max_length=15, null=True),
        ),
    ]
