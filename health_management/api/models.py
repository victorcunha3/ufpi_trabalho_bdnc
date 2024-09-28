from django.db import models
import json

import json

class Patient(models.Model):
    nome = models.CharField(max_length=100)
    historico_medico = models.TextField()
    sintomas = models.TextField()  # Aqui, armazena como JSON
    tratamentos = models.TextField()
