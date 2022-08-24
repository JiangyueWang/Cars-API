from django.urls import path
from cars import views

urlpatterns = [
    path('', views.cars_list),
    path('<int:pk>/', views.car_detail),
    path('query_param/', views.query_param)
]
