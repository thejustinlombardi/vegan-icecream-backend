from django.urls import path
from . import views

urlpatterns = [
    path('icecreams/', views.IceCreamList.as_view(), name='icecream_list'),
    path('icecreams/<int:pk>', views.IceCreamDetail.as_view(),
         name="icecream_detail"),
]
