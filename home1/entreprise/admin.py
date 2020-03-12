from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.SocialAccount)
admin.site.register(models.Equipe)
admin.site.register(models.Service)
admin.site.register(models.MessageAcceuil)
admin.site.register(models.Info)
admin.site.register(models.Temoignage)


