from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    '''Admin View for Cliente'''

    list_display = ('name',)
    list_filter = ('name',)
    