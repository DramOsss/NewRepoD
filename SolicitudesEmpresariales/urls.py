"""
URL configuration for SolicitudesEmpresariales project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Solicitudes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('home/', views.home, name='home'),
    path('ocupaciones/', views.ocupacion_list, name='ocupacion_list'),  
    path('ocupaciones/add/', views.ocupacion_form, name='ocupacion_add'), 
    path('ocupaciones/edit/<str:id_ocupacion>/', views.ocupacion_form, name='ocupacion_edit'),  
    path('ocupaciones/delete/<str:id_ocupacion>/', views.ocupacion_delete, name='ocupacion_delete'),
    path('egresados/', views.egresados_list, name='egresados_list'),  
    path('egresados/add/', views.egresado_form, name='egresado_add'), 
    path('egresados/edit/<str:id_egresado>/', views.egresado_form, name='egresado_edit'),  
    path('egresados/delete/<str:id_egresado>/', views.egresado_delete, name='egresado_delete'), 
    path('empresas/', views.empresas_list, name='empresas_list'),  
    path('empresas/add/', views.empresa_form, name='empresa_add'), 
    path('empresas/edit/<int:id_empresa>/', views.empresa_form, name='empresa_edit'),  
    path('empresas/delete/<int:id_empresa>/', views.empresa_delete, name='empresa_delete'),
    path('solicitudes/', views.solicitudes_list, name='solicitudes_list'),  
    path('solicitudes/add/', views.solicitud_form, name='solicitud_add'), 
    path('solicitudes/edit/<int:id_solicitud>/', views.solicitud_form, name='solicitud_edit'),  
    path('solicitudes/delete/<int:id_solicitud>/', views.solicitud_delete,name='solicitud_delete'), 
    path('solicitud/detalle/<int:id_solicitud>/', views.detalles_solicitud, name='detalles_solicitud'),
    path('solicitud/<int:id_solicitud>/actualizar_detalles/', views.actualizar_detalles, name='actualizar_detalles'),
]
