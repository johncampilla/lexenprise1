# Generated by Django 4.2.6 on 2024-07-23 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatter', '0039_alter_inboxmessage_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inboxmessage',
            name='status',
            field=models.CharField(blank=True, choices=[('UNREAD', 'UNREAD'), ('READ', 'READ')], default='UNREAD', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='tempchatmessages',
            name='status',
            field=models.CharField(blank=True, choices=[('UNREAD', 'UNREAD'), ('READ', 'READ')], default='UNREAD', max_length=15, null=True),
        ),
    ]
