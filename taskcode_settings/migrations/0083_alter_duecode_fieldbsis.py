# Generated by Django 4.2.6 on 2024-03-22 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0082_alter_activitycodes_trantype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Renewal Date', 'Renewal Date'), ('Document Receipt Date', 'Document Receipt Date'), ('IR Renewal Date', 'IR Renewal Date'), ('RunDate', 'RunDate'), ('OA Mailing Date', 'OA Mailing Date'), ('Document Date', 'Document Date'), ('Publication Date', 'PublicationDate'), ('Application Date', 'Application Date'), ('PCT Publication Date', 'PCT Publication Date'), ('PCT Filing Date', 'PCT Filing Date'), ('Priority Date', 'Priority Date'), ('IR_subsequentDate', 'IR_subsequentDate'), ('Registration Date', 'RegistrationDate'), ('IR Date', 'IR Date')], max_length=30, null=True),
        ),
    ]
