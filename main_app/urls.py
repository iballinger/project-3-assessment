from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/create/', views.ItemCreate.as_view(), name='item_create'),
    path('delete/<int:pk>', views.ItemDelete.as_view(), name='item_delete')
]