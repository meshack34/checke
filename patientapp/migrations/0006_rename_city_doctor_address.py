# Generated by Django 4.2.5 on 2023-09-28 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0005_patient_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='city',
            new_name='address',
        ),
    ]
