# Generated by Django 4.2.6 on 2024-04-16 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0105_alter_task_detail_doc_type_and_more'),
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
            field=models.CharField(blank=True, choices=[('IPO', 'IPO'), ('Mail', 'Mail'), ('Email', 'Email'), ('Personal', 'Personal'), ('Court', 'Court')], max_length=15, null=True),
        ),
    ]