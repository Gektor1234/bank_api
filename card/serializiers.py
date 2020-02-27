from rest_framework import serializers
from .models import Card, Transaction, MasterChek, Man
# создаем сериализайзер для отображение данных в списки питон

class TransactionSerializers(serializers.Serializer):
    number = serializers.IntegerField()
    balance = serializers.IntegerField()
    man_id = serializers.IntegerField()
    time_transaction = serializers.TimeField()
    date_transaction = serializers.DateField()

class CardSerializers(serializers.Serializer):
    number = serializers.IntegerField()
    balance = serializers.IntegerField()
    man_id = serializers.IntegerField()

    def create(self, validated_data): # метод для сообщение инструкции при вызове метода "save"
        return Card.objects.create(**validated_data), Transaction.objects.create(**validated_data)

    def update(self, instance, validated_data): # метод для обновления данных (переназначаем значения либо сохраняем старое)
        instance.number = validated_data.get('number', instance.number)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.man_id = validated_data.get('man_id', instance.man_id)
        instance.save()
        return instance, Transaction.objects.create(**validated_data)

class MasterSerializiers(serializers.Serializer):
    man_id = serializers.IntegerField()
    balance = serializers.IntegerField()

    def create(self, validated_data):
        return MasterChek.objects.create(**validated_data),Transaction.objects.create(**validated_data)

    def update(self, instance, validated_data): # метод для обновления данных (переназначаем значения либо сохраняем старое)
        instance.man_id = validated_data.get('man_id', instance.man_id)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.save()
        return instance, Transaction.objects.create(**validated_data)

class ManSerializiers(serializers.Serializer):
    name = serializers.CharField(max_length=128)

    def create(self, validated_data):
        return Man.objects.create(**validated_data)

