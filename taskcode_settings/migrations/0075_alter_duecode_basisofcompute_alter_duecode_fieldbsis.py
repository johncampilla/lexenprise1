# Generated by Django 4.2.6 on 2024-03-20 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskcode_settings', '0074_alter_activitycodes_trantype_and_more'),
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
            field=models.CharField(blank=True, choices=[('OA Mailing Date', 'OA Mailing Date'), ('Document Receipt Date', 'Document Receipt Date'), ('Registration Date', 'RegistrationDate'), ('Document Date', 'Document Date'), ('IR_subsequentDate', 'IR_subsequentDate'), ('IR Renewal Date', 'IR Renewal Date'), ('Application Date', 'Application Date'), ('PCT Filing Date', 'PCT Filing Date'), ('PCT Publication Date', 'PCT Publication Date'), ('Renewal Date', 'Renewal Date'), ('Priority Date', 'Priority Date'), ('IR Date', 'IR Date'), ('RunDate', 'RunDate'), ('Publication Date', 'PublicationDate')], max_length=30, null=True),
        ),
    ]