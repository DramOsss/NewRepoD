# Generated by Django 5.1.2 on 2024-10-26 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Solicitudes', '0004_detallessolicitud_selected_egresado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallessolicitud',
            name='estatus_detalle',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Pendiente'), (2, 'En Proceso'), (3, 'Completado'), (4, 'Cancelado')], null=True),
        ),
    ]
