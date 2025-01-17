# Generated by Django 4.2.6 on 2024-08-15 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0142_alter_task_detail_billstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='billstatus',
            field=models.CharField(blank=True, choices=[('Billed', 'Billed'), ('Unbilled', 'Unbilled')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='doc_type',
            field=models.CharField(blank=True, choices=[('Incoming', 'Incoming'), ('Others', 'Others'), ('Outgoing', 'Outgoing')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Personal', 'Personal'), ('Mail', 'Mail'), ('Email', 'Email'), ('IPO', 'IPO'), ('Court', 'Court')], max_length=15, null=True),
        ),
    ]
