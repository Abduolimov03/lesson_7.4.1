from django.urls import path
from .views import ListCreateApi, DetailDeleteUpdateApi
urlpatterns = [
    path('', ListCreateApi.as_view(), name='watch-list'),
    path('detail/<int:pk>/', DetailDeleteUpdateApi.as_view(), name='watch-detail')
]