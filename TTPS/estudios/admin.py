from django.contrib import admin
from . import models

admin.site.register(models.SampleSet)
admin.site.register(models.Enfermedad)
admin.site.register(models.Estudio)