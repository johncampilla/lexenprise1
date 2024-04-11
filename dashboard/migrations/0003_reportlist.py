# Generated by Django 4.2.6 on 2024-02-25 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_lookup', '0003_activitygroup_seq'),
        ('dashboard', '0002_numberofmattersbynature'),
    ]

    operations = [
        migrations.CreateModel(
            name='reportlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportgroup', models.CharField(blank=True, choices=[('Client', 'Client'), ('Matters', 'Matters'), ('Due Dates', 'Due Dates'), ('Invoices', ' Invoices'), ('Activities', 'Activites')], max_length=20, null=True)),
                ('reportdetail', models.CharField(blank=True, max_length=200, null=True)),
                ('casetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference_lookup.casetype')),
            ],
            options={
                'verbose_name_plural': 'Report List',
            },
        ),
    ]
