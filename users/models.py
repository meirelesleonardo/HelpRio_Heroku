from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.instituicao.models import Instituicao

class User(AbstractUser):
    Instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.first_name