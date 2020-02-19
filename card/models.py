from django.db import models


# Создание моделей держателя карты и самой карты в админпанельке.
class Man(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Card(models.Model):
    number = models.PositiveIntegerField(default=0) # номер карты
    balance = models.PositiveIntegerField(default=0) # баланс
    man = models.ForeignKey('Man', related_name='cards', on_delete=models.CASCADE)   # держатель карты

    class Meta:
        managed = True
        db_table = 'card'
        constraints = [
            models.CheckConstraint(check=models.Q(balance__gte='0'), name='card_balance_non_negative'),
        ]

class Transaction(models.Model):
    number = models.PositiveIntegerField(default=0)
    balance = models.PositiveIntegerField(default=0)
    man = models.ForeignKey('Man', related_name='transaction', on_delete=models.CASCADE)




