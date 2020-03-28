from django.contrib import admin
from . import models

from django.utils.safestring import mark_safe

from actions import Actions

# Register your models here.
class SocialAccountAdmin(Actions):
    fieldsets = [
        ('Presentation',{'fields': ['icon','nom']}),
        ('Standard', {'fields': ['lien']}),
        ('Status', {'fields': ['status']})
    ]
    
    
    list_display = ('icon','nom','date_add','status')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    readonly_fields = ['nom','date_add']

    

                                                                                                                                  
    
    
class EquipeAdmin(Actions):
    fieldsets = [
        ('Presentation',{'fields': ['nom','prenom']}),
        ('Presentation',{'fields': ['image','poste','message']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    
    list_display = ('nom','prenom','date_add','status')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    
    def image_views(self,obj):
        return mark_safe("<img src='{url}' width= 100px height=50px >".format(url=obj.image.url))
    
class ServiceAdmin(Actions):
    fieldsets = [
        ('Presentation',{'fields': ['nom','description']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    list_display = ('nom','date_add','status')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10

class MessageAcceuilAdmin(Actions):
    fieldsets = [
        ('Presentation',{'fields': ['video','sujet','message']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    list_display = ('video','date_add','status')
    list_filter = ('status',)
    search_fields = ('video',)
    date_hierarchy = "date_add"
    list_display_links = ['video']
    ordering = ['video']
    list_per_page = 10
    
    
    
class InfoAdmin(Actions):
    fieldsets = [
        ('Presentation',{'fields': ['numero','address']}),
        ('Compte',{'fields': ['email','site']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    list_display = ('numero','date_add','status')
    list_filter = ('status',)
    search_fields = ('numero',)
    date_hierarchy = "date_add"
    list_display_links = ['numero']
    ordering = ['numero']
    list_per_page = 10
    
class TemoignageAdmin(Actions):
    fieldsets = [
        ('Presentation',{'fields': ['nom','prenom','image']}),
        ('Poste',{'fields': ['travail','message']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    list_display = ('nom','date_add','status')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    readonly_fields = ['nom','date_add']

    
 def image_views(self,obj):
        return mark_safe("<img src='{url}' width= 100px height=50px >".format(url=obj.image.url))
    
    
def _register(model,Admin_class):
    admin.site.register(model,Admin_class)

_register(models.SocialAccount, SocialAccountAdmin)  
_register(models.Service, ServiceAdmin)  
_register(models.Equipe, EquipeAdmin)   
_register(models.Info, InfoAdmin)  
_register(models.MessageAcceuil, MessageAcceuilAdmin)  
_register(models.Temoignage, TemoignageAdmin)  


