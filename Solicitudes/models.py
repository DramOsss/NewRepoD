from django.contrib.auth.models import User
from django.db import models

class Ocupaciones(models.Model):
    id_ocupacion = models.CharField(primary_key=True, max_length=6)
    nombre_ocupacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_ocupacion +' - '+ self.id_ocupacion

class Egresados(models.Model):
    id_egresado = models.CharField(primary_key=True, max_length=15)
    nombre_egresado = models.CharField(max_length=30)
    apellido_egresado = models.CharField(max_length=30)
    direccion_egresado = models.CharField(max_length=100, blank=True, null=True)
    telefono_egresado = models.CharField(max_length=15, blank=True, null=True) 
    email_egresado = models.EmailField(max_length=100, blank=True, null=True) 
    estatus_egresado = models.BooleanField(verbose_name="Estatus del egresado", default=False)
    id_ocupacion = models.ForeignKey(Ocupaciones, models.SET_NULL, db_column='id_ocupacion', blank=True, null=True)

    def __str__(self):
        return f'{self.nombre_egresado} {self.apellido_egresado}'

class Empresas(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=100)
    direccion_empresa = models.CharField(max_length=100, blank=True, null=True)
    telefono_empresa = models.CharField(max_length=15, blank=True, null=True)
    email_empresa = models.EmailField(max_length=100, blank=True, null=True)  

    def __str__(self):
        return self.nombre_empresa
    

class SolicitudesServicio(models.Model):
    ESTATUS_CHOICES = [
        (1, 'Pendiente'),
        (2, 'En Proceso'),
        (3, 'Completado'),
    ]
    id_solicitud = models.AutoField(primary_key=True)
    fecha_solicitud = models.DateField(blank=True, null=True)
    id_empresa = models.ForeignKey(Empresas, models.SET_NULL, db_column='id_empresa', blank=True, null=True)
    id_ocupacion = models.ForeignKey(Ocupaciones, models.SET_NULL, db_column='id_ocupacion', blank=True, null=True)
    perfil_solicitud = models.TextField(blank=True, null=True)
    estatus_solicitud = models.SmallIntegerField(choices=ESTATUS_CHOICES, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, db_column='id_usuario', blank=True, null=True)

    def __str__(self):
        return f'Solicitud {self.id_solicitud} - {self.id_empresa}'

class DetallesSolicitud(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_solicitud = models.ForeignKey(SolicitudesServicio, models.CASCADE, db_column='id_solicitud', 
                                     blank=True, null=True, related_name='detalles_solicitud')
    id_egresado = models.ForeignKey(Egresados, models.CASCADE, db_column='id_egresado', blank=True, null=True)
    estatus_solicitud = models.ForeignKey(SolicitudesServicio, models.CASCADE, db_column='estatus_solicitud', 
                                          blank=True, null=True, related_name='estatus_detalles')
    selected_egresado = models.BooleanField(default=False)
    def __str__(self):
        return f'Detalle {self.id_detalle} - Solicitud {self.id_solicitud}'

