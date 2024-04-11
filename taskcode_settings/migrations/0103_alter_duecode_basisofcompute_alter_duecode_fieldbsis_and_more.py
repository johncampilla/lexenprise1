# Generated by Django 4.2.6 on 2024-04-08 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0102_alter_activitycodes_trantype_and_more'),
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
            field=models.CharField(blank=True, choices=[('Document Receipt Date', 'Document Receipt Date'), ('Application Date', 'Application Date'), ('Publication Date', 'PublicationDate'), ('IR_subsequentDate', 'IR_subsequentDate'), ('Document Date', 'Document Date'), ('PCT Filing Date', 'PCT Filing Date'), ('IR Renewal Date', 'IR Renewal Date'), ('IR Date', 'IR Date'), ('Registration Date', 'RegistrationDate'), ('PCT Publication Date', 'PCT Publication Date'), ('RunDate', 'RunDate'), ('Priority Date', 'Priority Date'), ('OA Mailing Date', 'OA Mailing Date'), ('Renewal Date', 'Renewal Date')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='basisofcompute',
            field=models.CharField(blank=True, choices=[('In Years', 'In Years'), ('In Days', 'In Days'), ('In Months', 'In Months')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='duecode_incoming',
            name='fieldbsis',
            field=models.CharField(blank=True, choices=[('Document Date', 'doc_date'), ('Mailing Date', 'mailing_date'), ('Date Receipt', 'tran_date')], max_length=30, null=True),
        ),
    ]
