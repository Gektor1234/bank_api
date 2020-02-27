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

class RealSwap(APIView):
    def put(self, request,pk,pk1): # изменение баланса либо любого другого параметра карты
        try:
            masterchek = get_object_or_404(MasterChek.objects.filter(man_id=pk))
            masterchek1 = get_object_or_404(MasterChek.objects.filter(man_id=pk1))
            c = masterchek1.balance
            b = masterchek.balance
            data1 = request.data.get('master')
            cc = data1.get('balance')
            ww =data1.get('balance')
            c = c + ww
            ww=c
            b = b - cc
            cc = b
            r ={'man_id':pk, 'balance':cc}
            f = {'man_id':pk1,'balance': ww}
            serializier_old = MasterSerializiers(instance=masterchek, data=r)
            serializier_old1 = MasterSerializiers(instance=masterchek1,data=f)
            if serializier_old.is_valid(raise_exception=True):
                masterchek = serializier_old.save()
            if serializier_old1.is_valid(raise_exception=True):
                masterchek1 = serializier_old1.save()
            return Response({'result':'ok', 'date': today.strftime("%Y-%m-%d-%H.%M.%S")})   # подтверждение перевода,дата и время
        except IntegrityError:
            return HttpResponse("Ошибка: Введены не корректные данные!")


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


