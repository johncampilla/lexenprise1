# Generated by Django 4.2.6 on 2024-07-23 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0122_alter_task_detail_billstatus_and_more'),
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
            field=models.CharField(blank=True, choices=[('IPO', 'IPO'), ('Personal', 'Personal'), ('Court', 'Court'), ('Email', 'Email'), ('Mail', 'Mail')], max_length=15, null=True),
        ),
    ]
