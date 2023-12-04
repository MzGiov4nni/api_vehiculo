from django.db import models

# Create your models here.
class Registro_vehiculo(models.Model):
    Propietario=models.CharField(max_length=100)
    Marca=models.CharField(max_length=100)
    Modelo=models.CharField(max_length=100)
    Año_vehiculo=models.PositiveBigIntegerField()
    

    class Meta:
        db_table = 'Registro_vehiculos'

    def __str__(self) -> str:
        return self.Nombre_Completo