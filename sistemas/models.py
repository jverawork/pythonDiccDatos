from django.db import models
from datetime import datetime
# Create your models here.
class cmd_basesdatos_t(models.Model):
    TIPBDD = (
        ('1', 'Under 09s'),
        ('2', 'Under 10s'),
        ('3', 'Under 11s')
    )

    TIPESTADOS = (
        ('A', 'Activo'),
        ('I', 'Inactivo')
    )

    id_bd = models.AutoField(primary_key=True)
    cod_bd = models.CharField(max_length=30, null=True, help_text = "Codigo de la Bdd")
    descripcion = models.CharField(max_length=200, null=True)
    estado = models.CharField(max_length=1, null=True, default = 'A', choices=TIPESTADOS)
    tipo_bd = models.CharField(max_length=30, null=True, choices=TIPBDD)
    bd_default = models.CharField(max_length=1, null=True)
    fec_creacion = models.DateTimeField(null=True, default = datetime.now())
    usu_creacion = models.CharField(max_length=30, null=True)
    ip_equipo = models.CharField(max_length=40, null=True)

    # Add the remaining fields of the model

    def __str__(self):
        return str(self.id_bd)
    
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular del modelo.
        """
        return reverse('model-detail-view', args=[str(self.id)])
