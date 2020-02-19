from django.urls import path

from .views import CardView, TransactionView, AddCard, ChangeCard, DeleteCard
app_name = 'Cards'

# создание url-адрес для получения доступа к методам
urlpatterns = [
    path('cards/', CardView.as_view()),
    path('add/', AddCard.as_view()),
    path('change/<int:pk>', ChangeCard.as_view()),
    path('delete/<int:pk>', DeleteCard.as_view()),
    path('transaction/<int:pk>', TransactionView.as_view()),
]