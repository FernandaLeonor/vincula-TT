from django.contrib import admin
from .models import TrabajosTerminales

@admin.register(TrabajosTerminales)
class TrabajosTerminalesAdmin(admin.ModelAdmin):
    pass