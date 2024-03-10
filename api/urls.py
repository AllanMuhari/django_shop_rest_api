from django.urls import path
from .views import LocationList, LocationDetail, ItemList, ItemDetail

urlpatterns = [
    path('location/', LocationList.as_view(), name='location-list'),
    path('location/<int:pk>/', LocationDetail.as_view(), name='location-detail'),
    path('item/', ItemList.as_view(), name='item-list'),
    path('item/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
]
