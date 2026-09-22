from django.db import models

class Propietario(models.Model):
    identificacion = models.IntegerField()
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=8)
    
    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre=models.CharField(max_length=100)
    especie=models.CharField(max_length=200)
    raza=models.CharField(max_length=200)
    fecha_nacimiento=models.CharField(max_length=200)
    peso=models.IntegerField()
    activo = models.BooleanField(default=True)
    propietario_id = models.IntegerField()

    def __str__(self):
            return self.nombre

class ConsultaVeterinaria(models.Model):
    mascota_id=models.CharField(max_length=100)
    fecha=models.CharField(max_length=200)
    motivo=models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=200)
    tratamiento = models.CharField(max_length=200)
    costo=models.IntegerField()


    def __str__(self):
        return self.motivo


