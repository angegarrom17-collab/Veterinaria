from rest_framework import serializers
from .models import Propietario, Mascota, ConsultaVeterinaria


class PropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propietario
        fields = '__all__'

    def validate_identificacion(self, value):
        if not value:  
            raise serializers.ValidationError('La identificacion no puede estar vacía.')
        return value

    def validate_nombre(self, value):
        if not value:
            raise serializers.ValidationError("El nombre no puede estar vacío.")
        return value


class MascotaSerializer(serializers.ModelSerializer):

    nombre = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        model = Mascota
        fields = '__all__'

    def validate_peso(self, value):
        if value is None or float(value) <= 0:
            raise serializers.ValidationError('El peso debe ser mayor a 0.')
        return value

    def validate_nombre(self, value):
        if not value or not str(value).strip():
            raise serializers.ValidationError('El nombre de la mascota no puede quedar vacío.')
        return value

    def validate_propietario(self, value):
        if value is None:
            raise serializers.ValidationError('La mascota debe de tener un propietario.')
        return value

class ConsultaVeterinariaSerializer(serializers.ModelSerializer):

    motivo = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        model = ConsultaVeterinaria
        fields = '__all__'

    def validate_costo(self, value):
        if value is None or float(value) < 0:
            raise serializers.ValidationError('El costo debe ser mayor o igual a 0.')
        return value

    def validate_motivo(self, value):
        if not value:
            raise serializers.ValidationError('La consulta debe de tener un motivo.')
        return value