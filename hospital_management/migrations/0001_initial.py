# Generated by Django 3.0.5 on 2022-04-16 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PatientInfoNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('mobile', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(blank=True, max_length=250, null=True)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.TextField(blank=True, max_length=250)),
                ('complaint', models.TextField(blank=True, max_length=250)),
                ('pulse', models.CharField(blank=True, max_length=3)),
                ('bp', models.CharField(blank=True, max_length=3)),
                ('bsl', models.CharField(blank=True, max_length=3)),
                ('temprature', models.CharField(blank=True, max_length=3)),
                ('general_exam', models.CharField(blank=True, max_length=250)),
                ('medicine_type1', models.CharField(blank=True, max_length=100)),
                ('medicine_name1', models.CharField(blank=True, max_length=100)),
                ('medicine_units1', models.CharField(blank=True, max_length=3)),
                ('medicine_detail1', models.CharField(blank=True, max_length=50)),
                ('medicine_type2', models.CharField(blank=True, max_length=100)),
                ('medicine_name2', models.CharField(blank=True, max_length=100)),
                ('medicine_units2', models.CharField(blank=True, max_length=3)),
                ('medicine_detail2', models.CharField(blank=True, max_length=50)),
                ('medicine_type3', models.CharField(blank=True, max_length=100)),
                ('medicine_name3', models.CharField(blank=True, max_length=100)),
                ('medicine_units3', models.CharField(blank=True, max_length=3)),
                ('medicin_detail3', models.CharField(blank=True, max_length=50)),
                ('medicine_type4', models.CharField(blank=True, max_length=100)),
                ('medicine_name4', models.CharField(blank=True, max_length=100)),
                ('medicine_units4', models.CharField(blank=True, max_length=3)),
                ('medicine_detail4', models.CharField(blank=True, max_length=50)),
                ('medicine_type5', models.CharField(blank=True, max_length=100)),
                ('medicine_name5', models.CharField(blank=True, max_length=100)),
                ('medicine_units5', models.CharField(blank=True, max_length=3)),
                ('medicine_detail5', models.CharField(blank=True, max_length=50)),
                ('other_information', models.TextField(blank=True, max_length=200)),
                ('total_bill', models.IntegerField(blank=True, null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
