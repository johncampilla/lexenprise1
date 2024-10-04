# Generated by Django 4.2.6 on 2024-07-25 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0126_alter_duecode_basisofcompute_alter_duecode_fieldbsis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duecode',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Years', 'In Years'), ('In Days', 'In Days'), ('In Months', 'In Months')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('OA Mailing Date', 'OA Mailing Date'), ('RunDate', 'RunDate'), ('IR Date', 'IR Date'), ('IR Renewal Date', 'IR Renewal Date'), ('Document Date', 'Document Date'), ('IR_subsequentDate', 'IR_subsequentDate'), ('Priority Date', 'Priority Date'), ('Document Receipt Date', 'Document Receipt Date'), ('PCT Publication Date', 'PCT Publication Date'), ('Application Date', 'Application Date'), ('PCT Filing Date', 'PCT Filing Date'), ('Registration Date', 'RegistrationDate'), ('Publication Date', 'PublicationDate'), ('Renewal Date', 'Renewal Date')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Years', 'In Years'), ('In Days', 'In Days'), ('In Months', 'In Months')], max_length=15, null=True),
        ),
    ]