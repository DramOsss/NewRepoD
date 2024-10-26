from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from SolicitudesEmpresariales import settings
from .models import Ocupaciones, Egresados, Empresas, SolicitudesServicio, DetallesSolicitud
from .forms import OcupacionForm, EgresadoForm, EmpresaForm,SolicitudesServicioForm, SolicitudDetalleForm




def index(request):
    return render(request, 'index.html')

@login_required
def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:

        if request.POST['password1'] == request.POST['password2']:
            # Register User
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('signin')
            except Exception as e:
                return render(request, 'signup.html', {'form': UserCreationForm,
                                                       'error': e})        
        return render(request, 'signup.html', {'form': UserCreationForm,
                                               'error': 'Contraseñas no coinciden'})

@login_required
def signout(request):
    logout(request)
    return redirect('index')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('home')
        

# Creando Mantenimientos

#Ocupaciones 
@login_required
def ocupacion_list(request):
    if request.method == 'GET':
        ocupaciones = Ocupaciones.objects.all()
        return render(request, 'ocupaciones.html', {'ocupaciones': ocupaciones})

@login_required
def ocupacion_form(request, id_ocupacion=None):
    print(f"ID Ocupacion: {id_ocupacion} ")
    if id_ocupacion:
        ocupacion = get_object_or_404(Ocupaciones, pk=id_ocupacion)
        print(f"Ocupacion: {ocupacion} ")
    else:
        ocupacion = None  
        print(f"Nueva ocupacion")
    
    if request.method == 'POST':
        form = OcupacionForm(request.POST, instance=ocupacion)
        if form.is_valid():
            new_ocupacion = form.save(commit=False)
            new_ocupacion.save()
            return redirect('ocupacion_list') 
    else:
        form = OcupacionForm(instance=ocupacion)  
    return render(request, 'ocupaciones_detalles.html', {'form': form, 'ocupacion': ocupacion})

@login_required
def ocupacion_delete(request, id_ocupacion):
    ocupacion = get_object_or_404(Ocupaciones, pk=id_ocupacion)
    
    if request.method == 'POST':
        ocupacion.delete()
        return redirect('ocupacion_list')  
    
    return render(request, 'ocupacion_confirm_delete.html', {'ocupacion': ocupacion})

#Egresados
@login_required
def egresados_list(request):
    if request.method == 'GET':
        egresados = Egresados.objects.all()
        return render(request, 'egresados.html', {'egresados': egresados})

@login_required
def egresado_form(request, id_egresado=None):
    print(f"ID Egresado: {id_egresado} ")
    if id_egresado:
        egresado = get_object_or_404(Egresados, pk=id_egresado)
        print(f"Egresado: {egresado} ")
    else:
        egresado = None  
        print(f"Nuevo egresado")
    
    if request.method == 'POST':
        form = EgresadoForm(request.POST, instance=egresado)
        if form.is_valid():
            new_egresado = form.save(commit=False)
            new_egresado.save()
            return redirect('egresados_list') 
    else:
        form = EgresadoForm(instance=egresado)  
    return render(request, 'egresados_detalles.html', {'form': form, 'egresado': egresado})

@login_required
def egresado_delete(request, id_egresado):
    egresado = get_object_or_404(Egresados, pk=id_egresado)
    
    if request.method == 'POST':
        egresado.delete()
        return redirect('egresados_list')  
    
    return render(request, 'egresado_confirm_delete.html', {'egresado': egresado})

#Empresas

@login_required
def empresas_list(request):
    if request.method == 'GET':
        empresas = Empresas.objects.all()
        return render(request, 'empresas.html', {'empresas': empresas})

@login_required
def empresa_form(request, id_empresa=None):
    print(f"ID Empresas: {id_empresa} ")
    if id_empresa:
        empresa = get_object_or_404(Empresas, pk=id_empresa)
        print(f"Empresa: {empresa} ")
    else:
        empresa = None  
        print(f"Nuevo empresa")
    
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            new_empresa = form.save(commit=False)
            new_empresa.save()
            return redirect('empresas_list') 
    else:
        form = EmpresaForm(instance=empresa)  
    return render(request, 'empresas_detalles.html', {'form': form, 'empresa': empresa})

@login_required
def empresa_delete(request, id_empresa):
    empresa = get_object_or_404(Empresas, pk=id_empresa)
    
    if request.method == 'POST':
        empresa.delete()
        return redirect('empresas_list')  
    
    return render(request, 'empresa_confirm_delete.html', {'empresa': empresa})


#Solicitudes
@login_required
def solicitudes_list(request):
    if request.method == 'GET':
        solicitudes = SolicitudesServicio.objects.all()
        return render(request, 'solicitudes.html', {'solicitudes': solicitudes})

@login_required
def solicitud_form(request, id_solicitud=None):
    
    if id_solicitud:
        solicitud = get_object_or_404(SolicitudesServicio, pk=id_solicitud)
        print(f"Solicitud: {solicitud}")
        detalles_egresados = DetallesSolicitud.objects.filter(id_solicitud=solicitud).select_related('id_egresado')
    else:
        solicitud = None
        detalles_egresados = None
        print(f"Nueva solicitud")

    if request.method == 'GET':
        form = SolicitudesServicioForm(instance=solicitud)
        
    else:
        form = SolicitudesServicioForm(request.POST, instance=solicitud)

        if form.is_valid():
            new_solicitud = form.save(commit=False)
            new_solicitud.fecha_solicitud = timezone.now()
            new_solicitud.estatus_solicitud = 1
            new_solicitud.save()  

            egresados_relacionados = Egresados.objects.filter(id_ocupacion=new_solicitud.id_ocupacion)
            print(egresados_relacionados)

            if egresados_relacionados.count() < 1:
                delete_detalle = DetallesSolicitud.objects.filter(id_solicitud=new_solicitud.id_solicitud)
                delete_detalle.delete()
                print(f"Detalles eliminados para la solicitud {new_solicitud.id_solicitud}")
                    
        else:
            print("ERROR")
            return render(request, 'solicitudes_detalles.html', {'form': form})

        with transaction.atomic():

            for egresado in egresados_relacionados:
                print('Procesando detalle para el egresado:', egresado)

                # Actualizar o crear detalles
                detalle, creado = DetallesSolicitud.objects.update_or_create(
                    id_solicitud=new_solicitud,
                    estatus_solicitud = new_solicitud,
                    id_egresado=egresado
                )

                if creado:
                    print('Detalle creado para:', egresado)
                    
                    detalle.save()
                    print('Detalle actualizado con otros cambios.')

            return redirect('solicitudes_list')

    return render(request, 'solicitudes_detalles.html', {
        'form': form, 
        'solicitud': solicitud,
        'detalles_egresados': detalles_egresados
    })


@login_required
def solicitud_delete(request, id_solicitud):
    solicitud = get_object_or_404(SolicitudesServicio, pk=id_solicitud)
    
    if request.method == 'POST':
        solicitud.delete()
        return redirect('solicitudes_list')  
    
    return render(request, 'solicitud_confirm_delete.html', {'solicitud': solicitud})

@login_required
def detalles_solicitud(request, id_solicitud):
    solicitud = get_object_or_404(SolicitudesServicio, pk=id_solicitud)
    detalles = DetallesSolicitud.objects.filter(id_solicitud=solicitud)
    return render(request, 'detalles_solicitud.html', {
        'solicitud': solicitud,
        'detalles': detalles
    })

@login_required

def actualizar_detalles(request, id_solicitud):
    solicitud = get_object_or_404(SolicitudesServicio, pk=id_solicitud)
    selected_ids = request.POST.getlist('selected_egresados')

    if len(selected_ids) > 0:
        action = request.POST.get('action')
        if action == 'complete_request':
            try:
                with transaction.atomic():
                    detalles = DetallesSolicitud.objects.filter(id_solicitud=solicitud)

                    for detalle in detalles:
                        if str(detalle.id_detalle) in selected_ids:
                            # Marcar el egresado como seleccionado y enviar correo de aceptación
                            detalle.selected_egresado = True
                            send_mail(
                                'Solicitud Aceptada',
                                f'Estimado/a {detalle.id_egresado.nombre_egresado},\n\nSu solicitud ha sido aceptada para el perfil {solicitud.perfil_solicitud}.',
                                'from@example.com',  # Reemplaza con tu dirección de remitente
                                [detalle.id_egresado.email_egresado],
                                fail_silently=False,
                            )
                        else:
                            # Si no está seleccionado, restablecer el estatus y eliminar del detalle
                            detalle.id_egresado.estatus_egresado = True
                            detalle.id_egresado.save()
                            detalle.delete()

                    # Cambiar el estado de la solicitud a "Completado" (3)
                    solicitud.estado = 3
                    solicitud.save()

                    messages.success(request, "La solicitud ha sido completada exitosamente y los correos fueron enviados a los seleccionados.")
                    print("Actualización completada exitosamente")

            except Exception as e:
                print(f"Error durante la actualización: {e}")
                messages.error(request, f"Error durante la actualización: {e}")
                return redirect('detalles_solicitud', id_solicitud=id_solicitud)

            return redirect('detalles_solicitud', id_solicitud=id_solicitud)
        
        else:
            try:
                with transaction.atomic():
                    detalles = DetallesSolicitud.objects.filter(id_solicitud=solicitud)
                    
                    if detalles.exists():
                        for detalle in detalles:
                            if str(detalle.id_detalle) in selected_ids:
                                detalle.selected_egresado = True
                                send_mail(
                                    'Notificación de Solicitud',
                                    'Estimado/a {},\n\nSe le ha seleccionado para la solicitud {}.'.format(detalle.id_egresado.nombre_egresado, solicitud.perfil_solicitud),
                                    'from@example.com',  
                                    [detalle.id_egresado.email_egresado],   
                                    fail_silently=False,
                                )
                            else:
                                detalle.selected_egresado = False

                            # Actualiza el estatus de detalle y guarda
                            detalle.estatus_detalle = 2
                            detalle.save()

                            detalle.id_egresado.estatus_egresado = False
                            detalle.id_egresado.save()

                        solicitud.estado = 2
                        solicitud.save()

                        messages.success(request, "Correos enviados y estados actualizados correctamente.")
                        print("Actualización completada exitosamente")

                    else:
                        messages.error(request, "No seleccionaste ningún egresado.")
                        return redirect('detalles_solicitud', id_solicitud=id_solicitud)

            except Exception as e:
                print(f"Error durante la actualización: {e}")
                messages.error(request, f"Error durante la actualización: {e}")
                return redirect('detalles_solicitud', id_solicitud=id_solicitud)
    
    else:
        messages.error(request, "No seleccionaste ningún egresado.")
        return redirect('detalles_solicitud', id_solicitud=id_solicitud)

    return redirect('detalles_solicitud', id_solicitud=id_solicitud)

