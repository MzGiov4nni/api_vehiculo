# Generated by Django 4.2.6 on 2023-12-04 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Propietario', models.CharField(max_length=100)),
                ('Marca', models.CharField(max_length=100)),
                ('Modelo', models.CharField(max_length=100)),
                ('Año_vehiculo', models.PositiveBigIntegerField()),
            ],
            options={
                'db_table': 'Registro_vehiculos',
            },
        ),
    ]
