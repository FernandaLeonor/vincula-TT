from django.db import models
from django.utils.translation import pgettext_lazy
from apps.application_user.models import User
from .validation import validate_file_size, validate_file_extension


class TrabajosTerminales(models.Model):
    titulo=models.TextField()
    numero_tt=models.CharField(max_length=13)
    autores=models.ManyToManyField(User)
    asesores=models.TextField()
    sinodales=models.TextField()
    escrito=models.FileField(upload_to="archivos/",validators=[validate_file_size, validate_file_extension])
    anio = models.PositiveBigIntegerField()
    palabras_clave=models.TextField()
    resumen=models.TextField()
    creado_por=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="trabajos_terminales")

    class Meta:
        db_table= "Trabajos_Terminales"
    def __str__(self):
        return f"{self.id} {self.titulo}"
    def es_duenio(self, usuario: User):
        return self.creado_por==usuario
