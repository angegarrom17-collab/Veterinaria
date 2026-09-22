from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import sesion_contador_view
from . import views


urlpatterns = [
    path('api/propietarios/', views.api_propietarios, name='api_propietarios'),
    path('api/mascotas/', views.api_mascotas, name='api_mascotas'),
    path('api/mascotas/<int:pk>/', views.detalle_mascota, name='detalle_mascota'),
    path('api/consultas/', views.api_consultas, name='api_consultas'),

    
    path('api/api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/perfil/', views.perfil, name='api_perfil'),
    path('api/estadisticas/', views.estadisticas, name='api_estadisticas'),

    path('api/sesion/', sesion_contador_view, name='api_sesion'),
]