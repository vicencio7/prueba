# Generated by Django 3.2.4 on 2021-07-04 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0002_delete_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.IntegerField(max_length=10000, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(max_length=9)),
                ('responsable', models.CharField(max_length=50)),
                ('parentesco', models.CharField(choices=[('1', 'Hermano(a)'), ('2', 'Conyuge'), ('3', 'Hijo(a)'), ('4', 'Padre'), ('5', 'Madre'), ('6', 'Abuelo(a)'), ('7', 'Amigo(a)'), ('8', 'Compañero(a) de trabajo')], max_length=50)),
            ],
        ),
    ]
