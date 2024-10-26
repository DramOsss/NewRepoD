from django import forms
from .models import Egresados,Empresas,Ocupaciones,SolicitudesServicio,DetallesSolicitud

class OcupacionForm(forms.ModelForm):
    class Meta:
        model = Ocupaciones
        fields = ['id_ocupacion','nombre_ocupacion']

class EgresadoForm(forms.ModelForm):
    class Meta:
        model = Egresados
        fields = ['id_egresado','nombre_egresado', 'apellido_egresado',
                  'direccion_egresado', 'telefono_egresado',
                  'email_egresado', 'estatus_egresado', 'id_ocupacion']
        


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresas
        fields = ['nombre_empresa','direccion_empresa',
                  'telefono_empresa','email_empresa']


class SolicitudesServicioForm(forms.ModelForm):
    class Meta:
        model = SolicitudesServicio
        fields = ['id_empresa','id_ocupacion'
                  ,'perfil_solicitud','usuario']

class SolicitudDetalleForm(forms.ModelForm):
    class Meta:
        model =  DetallesSolicitud
        fields = ['id_solicitud','id_egresado',
                  'estatus_solicitud','selected_egresado']

