# Generated by Django 3.2.20 on 2024-06-25 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45, null=True)),
                ('category', models.CharField(max_length=45, null=True)),
                ('type', models.CharField(max_length=45, null=True)),
                ('memory', models.IntegerField(null=True)),
                ('run_time', models.DateTimeField(null=True)),
                ('next_repair_time', models.DateField(null=True)),
                ('warranty_time', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=45, null=True)),
                ('weight', models.FloatField(null=True)),
                ('length1', models.FloatField(null=True)),
                ('length2', models.FloatField(null=True)),
                ('length3', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
                ('width', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FishGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=45, null=True)),
                ('number', models.CharField(max_length=45, null=True)),
                ('time', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HydrologicInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monitoring_time', models.DateField()),
                ('water_quality_category', models.CharField(blank=True, choices=[('Ⅰ', 'Ⅰ类'), ('Ⅱ', 'Ⅱ类'), ('Ⅲ', 'Ⅲ类'), ('Ⅳ', 'Ⅳ类'), ('Ⅴ', 'Ⅴ类')], max_length=20, null=True)),
                ('water_temperature', models.FloatField(blank=True, null=True)),
                ('pH', models.FloatField(blank=True, null=True)),
                ('dissolved_oxygen', models.FloatField(blank=True, null=True)),
                ('conductivity', models.FloatField(blank=True, null=True)),
                ('turbidity', models.FloatField(blank=True, null=True)),
                ('permanganate_index', models.FloatField(blank=True, null=True)),
                ('ammonia_nitrogen', models.FloatField(blank=True, null=True)),
                ('total_phosphorus', models.FloatField(blank=True, null=True)),
                ('total_nitrogen', models.FloatField(blank=True, null=True)),
                ('station_condition', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Hydrologic Information',
                'verbose_name_plural': 'Hydrologic Information',
            },
        ),
        migrations.CreateModel(
            name='NetCage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('width', models.FloatField(null=True)),
                ('length', models.FloatField(null=True)),
                ('depth', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='state',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('sensor_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20)),
                ('battery_level', models.PositiveIntegerField()),
                ('next_repair_time', models.DateTimeField()),
                ('warranty_time', models.DateField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.device')),
            ],
        ),
    ]
