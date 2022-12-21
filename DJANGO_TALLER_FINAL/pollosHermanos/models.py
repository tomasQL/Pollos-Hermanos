from django.db import models
from django.core import validators

# Create your models here.

class Reserva(models.Model):
    
    class Estados(models.TextChoices):
        RESERVADO='Reservado', 'Reservado'
        COMPLETADA='Completada', 'Completada'
        ANULADA='Anulada', 'Anulada'
        NOASISTEN='No asisten', 'No asisten'


    nombrePersona=models.CharField(max_length=50)
    telefono=models.IntegerField()
    fechaReserva=models.DateField()
    horaReserva=models.TimeField()
    cantidadPersonas=models.IntegerField(
        validators=[
            validators.MinValueValidator(limit_value=1, ),
            validators.MaxValueValidator(limit_value=15,)])
    estadoReserva=models.CharField(
        max_length=32,
        choices=Estados.choices)
    observacion=models.CharField(max_length=200)
