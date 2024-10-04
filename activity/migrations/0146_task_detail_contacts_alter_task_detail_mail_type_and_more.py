# Generated by Django 4.2.6 on 2024-09-13 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0021_alter_contact_person_address_and_more'),
        ('activity', '0145_alter_task_detail_billstatus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_detail',
            name='contacts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.contact_person'),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Court', 'Court'), ('Email', 'Email'), ('Personal', 'Personal'), ('Mail', 'Mail'), ('IPO', 'IPO')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='tran_type',
            field=models.CharField(blank=True, choices=[('Non-Billable', 'Non-Billable'), ('Billable', 'Billable')], max_length=15, null=True),
        ),
    ]
