from django.db import models

# Create your models here.

class Product(models.Model):
    NIVEL_CHOICES = [
        (1, "Nivel 1"),
        (2, "Nivel 2"),
        (3, "Nivel 3"),
        (4, "Nivel 4"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    level = models.IntegerField(choices=NIVEL_CHOICES)

    def __str__(self):
        return self.title

class Equipo_Status(models.Model):
    ROW_CHOICES = [
        (1, "Fila 1"),
        (2, "Fila 2"),
        (3, "Fila 3"),
        (4, "En Ruma"),
    ]
    locate = models.IntegerField(choices=ROW_CHOICES, default=4)
    nro_team = models.CharField(max_length=11,unique=True)
    type = models.CharField(max_length=4)
    line = models.CharField(max_length=4)
    type_load = models.CharField(max_length=20)
    deposit_days = models.IntegerField(default=0)
    status = models.CharField(max_length=30)

    def __str__(self):
        # Utiliza get_FIELD_display() para obtener el texto legible
        return f"{self.nro_team} - {self.get_locate_display()}"

    class Meta:
        verbose_name_plural = "Team Status"



