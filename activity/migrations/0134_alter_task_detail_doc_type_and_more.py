# Generated by Django 4.2.6 on 2024-07-26 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0133_alter_task_detail_doc_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_detail',
            name='doc_type',
            field=models.CharField(blank=True, choices=[('Others', 'Others'), ('Incoming', 'Incoming'), ('Outgoing', 'Outgoing')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='task_detail',
            name='mail_type',
            field=models.CharField(blank=True, choices=[('Court', 'Court'), ('Email', 'Email'), ('IPO', 'IPO'), ('Mail', 'Mail'), ('Personal', 'Personal')], max_length=15, null=True),
        ),
    ]
