from django.db import  transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializiers import CardSerializers, TransactionSerializers, MasterSerializiers,ManSerializiers
from .models import Card, Transaction, MasterChek, Man
from rest_framework.generics import get_object_or_404
from datetime import datetime
from django.db import IntegrityError
from django.shortcuts import HttpResponse

today = datetime.today()

class CardView(APIView):
    def get(self, request):  # информация о всех существующих картах
        cards = Card.objects.all()
        serializer = CardSerializers(cards, many=True)
        return Response({'cards': serializer.data})

class AddCard(APIView):
    def post(self, request):  # создание новой карты
        try:
            card = request.data.get('card')
            serializer = CardSerializers(data=card)
            if serializer.is_valid(raise_exception=True):
                card_saved = serializer.save()
            return Response({"result": 'ok', 'date': today.strftime("%Y-%m-%d-%H.%M.%S")})
        except IntegrityError:
            return HttpResponse("Ошибка: Введены не корректные данные!")

class ChangeCard(APIView):
    def put(self, request, pk): # изменение баланса либо любого другого параметра карты
        try:
            saved_card = get_object_or_404(Card.objects.all(), pk=pk)
            data = request.data.get('card')
            serializer = CardSerializers(instance=saved_card, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                saved_card = serializer.save()
            return Response({'result':'ok', 'date': today.strftime("%Y-%m-%d-%H.%M.%S")})   # подтверждение перевода,дата и время
        except IntegrityError:
            return HttpResponse("Ошибка: Введены не корректные данные!")

class DeleteCard(APIView):
    def delete(self, request, pk):    # удаление карты в случае ее просрочки
        card = get_object_or_404(Card.objects.all(), pk=pk)
        card.delete()
        return Response({'result': 'ok', 'date': today.strftime("%Y-%m-%d-%H.%M.%S")})

class TransactionView(APIView):
    def get(self, request, pk):  # информация о всех существующих картах
        transaction = Transaction.objects.filter(number=pk)
        serializer = CardSerializers(transaction, many=True)
        return Response({'transaction': serializer.data})


class MasterView(APIView):
    def get(self,request, pk):
        Masterchek = MasterChek.objects.filter(man=pk)
        serializir = MasterSerializiers(Masterchek,many=True)
        return Response({'Masterchek': serializir.data})

class AddMaster(APIView):
    def post(self, request):
        try:
            master = request.data.get('master')
            serializer1 = MasterSerializiers(data=master)
            if serializer1.is_valid(raise_exception=True):
                master_saved = serializer1.save()
            return Response({"result": 'ok', 'date': today.strftime("%Y-%m-%d-%H.%M.%S")})
        except IntegrityError:
            return HttpResponse("Ошибка: Введены не корректные данные!")

class Simple_Transaction(APIView):
    def put(self, request,pk,pk1): # изменение баланса либо любого другого параметра карты
        try:
            account = get_object_or_404(MasterChek.objects.filter(man_id=pk))
            account2 = get_object_or_404(MasterChek.objects.filter(man_id=pk1))
            user_balance2 = account2.balance
            user_balance = account.balance
            data = request.data.get('master')
            summa = data.get('balance')
            summa2 = data.get('balance')
            user_balance2 = user_balance2 + summa2
            summa2 = user_balance2
            user_balance = user_balance - summa
            summa = user_balance
            new_params = {'man_id': pk, 'balance': summa}
            new_params2 = {'man_id': pk1, 'balance': summa2}
            serializier_account = MasterSerializiers(instance=account, data=new_params)
            serializier_account2 = MasterSerializiers(instance=account2, data=new_params2)
            if serializier_account.is_valid(raise_exception=True):
                account = serializier_account.save()
            if serializier_account2.is_valid(raise_exception=True):
                account2 = serializier_account2.save()
            return Response({'result':'ok', 'date': today.strftime("%Y-%m-%d-%H.%M.%S")})   # подтверждение перевода,дата и время
        except IntegrityError:
            return HttpResponse("Ошибка: Нет денег Антон!")


class ShowMan(APIView):
    def get(self, request):
        man = Man.objects.all()
        serializire = ManSerializiers(man,many=True)
        return Response({'Mans':serializire.data})

class AddMan(APIView):
    def post(self,request):
        try:
            addman = request.data.get('man')
            serializir2 = ManSerializiers(data=addman)
            if serializir2.is_valid(raise_exception=True):
                man_saved = serializir2.save()
            return Response({"result": 'ok', 'date': today.strftime("%Y-%m-%d-%H.%M.%S")})
        except:
            return HttpResponse("Ошибка: Введены неверные данные!")


