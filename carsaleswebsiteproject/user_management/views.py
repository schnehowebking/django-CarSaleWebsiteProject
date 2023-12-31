from django.shortcuts import get_object_or_404, redirect, render

from car_management.models import Car, Order, Brand
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

# Create your views here.

class UserRegistrationView(CreateView):
    template_name = 'user_management/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    success_message = 'Registered successfully'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

class UserLoginView(LoginView):
    template_name = 'user_management/login.html'
    form_class = UserLoginForm
    next_page = reverse_lazy('homepage')
    success_message = 'Logged-In Successfully' 

    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class UserProfileView(LoginRequiredMixin, DetailView):
    template_name = 'user_management/profile.html'
    model = User

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.filter(user=self.request.user)
        context['orders'] = orders
        return context

class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user_management/password_change.html'
    form_class = UserChangePasswordwithoutForm
    success_url = reverse_lazy('profile')
    success_message = 'Password Changed Successfully'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'user_management/profile_update.html'
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    success_message = 'Profile Updated Successfully'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('profile')
    


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('homepage')
    success_message = 'Your are logged out!!'

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(self.request, self.success_message)
        return super().get(request, *args, **kwargs)
    

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'user_management/profile.html', {'orders': orders})

@login_required(login_url='login')
def buy_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.quantity -= 1
        car.save()
        Order.objects.create(user=request.user, car=car)

        messages.success(request, f'Car "{car.name}" purchased successfully.')
        return redirect('profile')

    return render(request, 'car_management/buy_car.html', {'car': car})


