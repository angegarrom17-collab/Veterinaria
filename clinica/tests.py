from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import PropietarioSerializer, MascotaSerializer, ConsultaVeterinariaSerializer


class VeterinariaPruebasAutomatizadas(APITestCase):

  def setUp(self):
    self.user_regular = User.objects.create_user(
        username='regular', password='Canela1'
    )
    self.user_admin = User.objects.create_superuser(
        username='admin', password ='Canela2'
    )

  def test_mascota_peso_cero_invalido(self):
    data = {
        'nombre': 'Firulais',
        'peso': 0,
        'especie': 'Perro',
        'propietario': 1,
    }
    serializer = MascotaSerializer(data=data)
    self.assertFalse(serializer.is_valid())
    self.assertIn('peso', serializer.errors)


  def test_consulta_costo_negativo_invalido(self):
    data = {'mascota': 1, 'motivo': 'Control', 'costo': -10.0}
    serializer = ConsultaVeterinariaSerializer(data=data)
    self.assertFalse(serializer.is_valid())
    self.assertIn('costo', serializer.errors)

  def test_perfil_usuario_anonimo_no_accede(self):
    url = '/clinica/api/perfil/'
    response = self.client.get(url)
    self.assertNotEqual(response.status_code, status.HTTP_200_OK)


  def test_perfil_usuario_autenticado_ok(self):
    url = '/clinica/api/perfil/'
    self.client.force_authenticate(user=self.user_regular)
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_estadisticas_permisos_admin(self):
    url = '/clinica/api/estadisticas/'

    self.client.force_authenticate(user=self.user_regular)
    response_regular = self.client.get(url)
    self.assertIn(
        response_regular.status_code,
        [status.HTTP_403_FORBIDDEN, status.HTTP_401_UNAUTHORIZED],
    )

    self.client.force_authenticate(user=self.user_admin)
    response_admin = self.client.get(url)
    self.assertEqual(response_admin.status_code, status.HTTP_200_OK)