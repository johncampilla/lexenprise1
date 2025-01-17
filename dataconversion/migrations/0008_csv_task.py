# Generated by Django 4.2.6 on 2024-03-20 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataconversion', '0007_alter_csv_matter_withpriority'),
    ]

    operations = [
        migrations.CreateModel(
            name='csv_task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClientNo', models.CharField(blank=True, max_length=15, null=True)),
                ('ApplicationNo', models.CharField(blank=True, max_length=25, null=True)),
                ('ActivityDate', models.DateField(blank=True, null=True)),
                ('seqno', models.CharField(blank=True, max_length=20, null=True)),
                ('TaskCode', models.CharField(blank=True, max_length=15, null=True)),
                ('TranType', models.CharField(blank=True, max_length=10, null=True)),
                ('DocumentCode', models.CharField(blank=True, max_length=10, null=True)),
                ('BillDate', models.DateField(blank=True, null=True)),
                ('TaskDescription', models.TextField(blank=True, null=True)),
                ('DocumentType', models.CharField(blank=True, max_length=10, null=True)),
                ('ActionType', models.CharField(blank=True, max_length=10, null=True)),
                ('CaseOfficer', models.CharField(blank=True, max_length=10, null=True)),
                ('Billed', models.CharField(blank=True, max_length=10, null=True)),
                ('ContactPerson', models.CharField(blank=True, max_length=60, null=True)),
                ('StageNo', models.CharField(blank=True, max_length=10, null=True)),
                ('MailOut', models.CharField(blank=True, max_length=10, null=True)),
                ('MailSent', models.CharField(blank=True, max_length=10, null=True)),
                ('DocumentPath', models.CharField(blank=True, max_length=100, null=True)),
                ('IpoFilingDate', models.DateField(blank=True, null=True)),
                ('GroupCode', models.CharField(blank=True, max_length=100, null=True)),
                ('LetterToClient', models.CharField(blank=True, max_length=10, null=True)),
                ('LetterToIPO', models.CharField(blank=True, max_length=10, null=True)),
                ('StampID', models.CharField(blank=True, max_length=60, null=True)),
                ('ModifiedBy', models.CharField(blank=True, max_length=60, null=True)),
                ('PaperNo', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
