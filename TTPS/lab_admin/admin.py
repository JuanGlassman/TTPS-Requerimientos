from django.contrib import admin
from . import models

admin.site.register(models.Presupuesto)
admin.site.register(models.Turno)
admin.site.register(models.Centro)
admin.site.register(models.LabAdmin)