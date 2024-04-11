# Generated by Django 4.2.6 on 2024-03-22 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0087_alter_duecode_basisofcompute_alter_duecode_fieldbsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Months', 'In Months'), ('In Years', 'In Years'), ('In Days', 'In Days')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Registration Date', 'RegistrationDate'), ('IR Renewal Date', 'IR Renewal Date'), ('Publication Date', 'PublicationDate'), ('Priority Date', 'Priority Date'), ('PCT Filing Date', 'PCT Filing Date'), ('Renewal Date', 'Renewal Date'), ('RunDate', 'RunDate'), ('IR_subsequentDate', 'IR_subsequentDate'), ('Application Date', 'Application Date'), ('IR Date', 'IR Date'), ('Document Date', 'Document Date'), ('OA Mailing Date', 'OA Mailing Date'), ('Document Receipt Date', 'Document Receipt Date'), ('PCT Publication Date', 'PCT Publication Date')], max_length=30, null=True),
        ),
    ]
