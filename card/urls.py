from django.urls import path

from .views import CardView, TransactionView

app_name = 'Cards'

# создание url-адрес для получения доступа к методам
urlpatterns = [
    path('cards/', CardView.as_view()),
    path('cards/<int:pk>', CardView.as_view()),
    path('transaction/<int:pk>', TransactionView.as_view()),
]