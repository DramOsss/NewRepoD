from django.contrib import admin
from django.contrib.auth.models import User
from .models import Ocupaciones, Egresados, Empresas, SolicitudesServicio, DetallesSolicitud

# Register your models here.

admin.site.register(Ocupaciones)
admin.site.register(Egresados)
admin.site.register(Empresas)
admin.site.register(SolicitudesServicio)
admin.site.register(DetallesSolicitud)