# Generated by Django 4.2.6 on 2024-03-22 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatter', '0020_alter_inboxmessage_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inboxmessage',
            name='status',
            field=models.CharField(blank=True, choices=[('READ', 'READ'), ('UNREAD', 'UNREAD')], default='UNREAD', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='tempchatmessages',
            name='status',
            field=models.CharField(blank=True, choices=[('READ', 'READ'), ('UNREAD', 'UNREAD')], default='UNREAD', max_length=15, null=True),
        ),
    ]
