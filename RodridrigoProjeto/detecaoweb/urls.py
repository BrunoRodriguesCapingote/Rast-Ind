from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('indentificacao/', views.indentificacao, name='indentificacao'),
    path('item_data', views.item_data, name='item_data'),
]