# Generated by Django 3.2.4 on 2021-07-04 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0003_paciente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='fecha_nacimiento',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(max_length=9),
        ),
    ]
