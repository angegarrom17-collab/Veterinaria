from django.contrib import admin
from .models import Propietario, Mascota, ConsultaVeterinaria

admin.site.register(Propietario)
admin.site.register(ConsultaVeterinaria)

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'propietario_id', 'peso', 'activo')