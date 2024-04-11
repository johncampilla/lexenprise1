# Generated by Django 4.2.6 on 2024-03-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0062_alter_activitycodes_trantype_alter_duecode_fieldbsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycodes',
            name='TranType',
            field=models.CharField(blank=True, choices=[('Billable', 'Billable'), ('Non-Billable', 'Non-Billable')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Priority Date', 'Priority Date'), ('OA Mailing Date', 'OA Mailing Date'), ('IR Renewal Date', 'IR Renewal Date'), ('PCT Filing Date', 'PCT Filing Date'), ('Document Date', 'Document Date'), ('PCT Publication Date', 'PCT Publication Date'), ('RunDate', 'RunDate'), ('Application Date', 'Application Date'), ('Renewal Date', 'Renewal Date'), ('Document Receipt Date', 'Document Receipt Date'), ('Registration Date', 'RegistrationDate'), ('Publication Date', 'PublicationDate'), ('IR Date', 'IR Date')], max_length=30, null=True),
        ),
    ]