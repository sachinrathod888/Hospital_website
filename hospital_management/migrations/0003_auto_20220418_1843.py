# Generated by Django 3.0.5 on 2022-04-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_management', '0002_patientinfonew_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfonew',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
