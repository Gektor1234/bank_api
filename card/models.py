from django.db import models

# Создание моделей держателя карты и самой карты в админпанельке.
class Man(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Card(models.Model):
    number = models.IntegerField() # номер карты
    balance = models.IntegerField() # баланс
    man = models.ForeignKey('Man', related_name='cards', on_delete=models.CASCADE)   # держатель карты




