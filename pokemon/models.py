from django.db import models
import uuid

# Create your models here.

class Pokemon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    name = models.CharField(max_length=100)
    pokedex_id = models.IntegerField()
    level = models.IntegerField(default=1)
    type_1 = models.CharField(max_length=50)
    type_2 = models.CharField(max_length=50, blank=True, null=True) 
    ability = models.CharField(max_length=100, blank=True) 

    nickname = models.CharField(max_length=100, blank=True, null=True)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')

    def __str__(self):
        display_name = self.nickname if self.nickname else self.name
        return f"{display_name} (Lvl {self.level})"
    
    '''
    null=False (Default) -> Il database obbliga ad avere un valore.
    blank=False (Default) -> Django obbliga a compilare il campo.
    "null=True, blank=True" -> Il campo è completamente opzionale ovunque.
    '''