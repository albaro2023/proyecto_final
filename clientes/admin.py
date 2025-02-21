from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'email',
        'telefono',
        'direccion',
        'created',
        'updated'
    )
    search_fields = ('nombre',)
    
admin.site.register(Cliente, ClienteAdmin)