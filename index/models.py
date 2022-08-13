from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.



class Factory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Şirkət adı')
    class Meta:
        ordering = ['title']
        verbose_name = 'Şirkət'
        verbose_name_plural = 'Şirkətlər'

    def __str__(self):
        return self.title
    



class Drug(models.Model):
    title = models.CharField(max_length=100, verbose_name='Başlıq')
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    price = models.IntegerField()
    expire = models.DateField()
    recipe_needed = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Dərmanlar'
        verbose_name = 'Dərman'

    def __str__(self):
        return self.title