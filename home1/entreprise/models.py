from django.db import models

# Create your models here.

class SocialAccount(models.Model):
    
    
    ICONS = [
        ("Twitter", "ion-logo-twitter"),
        ("Facebook", "ion-logo-facebook"),
        ("Instagram", "ion-logo-instagram")
        
    ]
    
    nom = models.CharField(max_length=255)
    lien = models.URLField()
    icon = models.CharField(choices=ICONS, max_length=20)

    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Social account'
        verbose_name_plural = 'Social account'

    def __str__(self):
        return self.nom
    
class Equipe(models.Model):
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/Equipe")
    poste = models.CharField(max_length=255)
    message = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        return self.nom
    
    
class Service(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.nom
    
    
class MessageAcceuil(models.Model):
    
    video = models.URLField()
    sujet = models.CharField(max_length=255)
    message = models.TextField()
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Message Acceuil'
        verbose_name_plural = 'Messages Acceuils'

    def __str__(self):
        return self.sujet
    
    
class Info(models.Model):
    address = models.CharField(max_length=255)
    numero = models.IntegerField()
    email = models.EmailField()
    site = models.URLField()
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Info'
        verbose_name_plural = 'Infos'

    def __str__(self):
        return self.nom
    
    
class Temoignage(models.Model):
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/Temoignage")
    travail = models.CharField(max_length=255)
    message = models.TextField()
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Temoignage'
        verbose_name_plural = 'Temoignages'

    def __str__(self):
        return self.nom
    
    
    
    
    
    
    
    
    
