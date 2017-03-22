from django.contrib import admin
from .models import Cliente, Equipo, Tecnico, Orden


admin.site.register(Cliente)
admin.site.register(Equipo)
admin.site.register(Tecnico)
admin.site.register(Orden)