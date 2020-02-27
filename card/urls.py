from django.urls import path

from .views import CardView, TransactionView, AddCard, ChangeCard, DeleteCard, MasterView,AddMaster,ShowMan,AddMan,RealSwap
app_name = 'Cards'

# создание url-адрес для получения доступа к методам
urlpatterns = [
    path('cards/', CardView.as_view()),
    path('add/', AddCard.as_view()),
    path('change/<int:pk>', ChangeCard.as_view()),
    path('delete/<int:pk>', DeleteCard.as_view()),
    path('transaction/<int:pk>', TransactionView.as_view()),
    path('Master/<int:pk>', MasterView.as_view()),
    path('Masteradd/', AddMaster.as_view()),
    path('Mans', ShowMan.as_view()),
    path('Addman',AddMan.as_view()),
    path('swap/<int:pk>',RealSwap.as_view()),
]