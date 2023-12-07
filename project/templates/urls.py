from django.urls import path # импортируем пути для установки маршрутов
from .views import index, about, contacts, form # импортируем функции визуализации из файла views

urlpatterns = [
    path('index/', index),
    path('about/',about),
    path('contacts/', contacts),
    path('form/', form),
]


