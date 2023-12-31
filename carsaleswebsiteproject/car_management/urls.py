from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('details/<int:pk>/', views.CarDetailsPageView.as_view(), name="carDetailspage"),
    path('shop/details/<int:pk>/', views.CarDetailsPageViewshop.as_view(), name="carDetailspageshop"),
    # path('user/<int:pk>/', views.buy_car, name='buy_car'),
    path('car/comment/<int:pk>/', views.add_comment, name='add_comment'),
    path('contact/', views.contactPage, name="contact"),
    path('shop/<slug:brand_slug>/', views.car_list, name='car_list_by_brand'),
    path('shop/', views.car_list, name="shoppage"),
    path('<slug:brand_slug>/', views.homepage, name='car_list_by_brand_index'),
]