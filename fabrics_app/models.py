from django.db import models


class FabricType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тип ткани'
        verbose_name_plural = 'Типы ткани'
        
        
class Fabric(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(max_length=500, verbose_name='Описание')
    color = models.CharField(max_length=200, verbose_name='Цвет')
    fabric_type = models.ManyToManyField(FabricType, verbose_name='Тип ткани')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ткань'
        verbose_name_plural = 'Ткани'   
        
        
    
