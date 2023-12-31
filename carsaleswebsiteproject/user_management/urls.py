from django.urls import path
from . import views
urlpatterns = [
    path('viewprofile/', views.UserProfileView.as_view(), name='profile'),
    path('viewprofile/', views.order_history),
    path('car/buy/<int:pk>/', views.buy_car, name='buy_car'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('change_password', views.UserPasswordChangeView.as_view(), name='change_password'),
    path('update_profile/<int:pk>/', views.UserProfileUpdateView.as_view(), name='update_profile'),
]
