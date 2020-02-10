from rest_framework.views import APIView
from rest_framework.response import Response
from .serializiers import CardSerializers
from .models import Card
from rest_framework.generics import get_object_or_404
from datetime import datetime


today = datetime.today()

class CardView(APIView):
    def get(self, request):  # информация о всех существующих картах
        cards = Card.objects.all()
        serializer = CardSerializers(cards, many=True)
        return Response({'cards': serializer.data})

    def post(self, request):  # создание новой карты
        card = request.data.get('card')
        serializer = CardSerializers(data=card)
        if serializer.is_valid(raise_exception=True):
            card_saved = serializer.save()
        return Response({"result": 'ok', 'date': today.strftime("%Y-%m-%d-%H.%M.%S")})

    def put(self, request, pk): # изменение баланса либо любого другого параметра карты
        saved_card = get_object_or_404(Card.objects.all(), pk=pk)
        data = request.data.get('card')
        serializer = CardSerializers(instance=saved_card, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            card_saved = serializer.save()
        return Response({'result':'ok', 'date': today.strftime("%Y-%m-%d-%H.%M.%S")})   # подтверждение перевода,дата и время

    def delete(self, request, pk):    # удаление карты в случае ее просрочки
        card = get_object_or_404(Card.objects.all(), pk=pk)
        card.delete()
        return Response({'result': 'ok', 'date': today.strftime("%Y-%m-%d-%H.%M.%S")})
