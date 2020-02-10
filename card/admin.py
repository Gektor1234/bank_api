from django.contrib import admin

from .models import Man,Card
# регистарция созданных моделей
admin.site.register(Man)
admin.site.register(Card)
