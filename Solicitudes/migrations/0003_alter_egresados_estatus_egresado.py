# Generated by Django 5.1.2 on 2024-10-24 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Solicitudes', '0002_remove_solicitudesservicio_id_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='egresados',
            name='estatus_egresado',
            field=models.BooleanField(default=False, verbose_name='Estatus del egresado'),
        ),
    ]
