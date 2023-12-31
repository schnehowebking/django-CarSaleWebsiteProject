from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import *
from .models import *

# Create your views here.
def homepage(request, brand_slug=None):
    cars = Car.objects.all()
    brands = Brand.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(slug = brand_slug)
        cars = Car.objects.filter(brand = brand)
    return render(request, 'car_management/index.html', {'cars':cars, 'brands':brands})

def car_list(request, brand_slug=None):
    cars = Car.objects.all()
    brands = Brand.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(slug = brand_slug)
        cars = Car.objects.filter(brand = brand)
    return render(request, 'car_management/car_list.html', {'cars':cars, 'brands':brands})


def contactPage(request):
    return render(request, './car_management/contact.html')


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class CarDetailsPageView(DetailView):
    model = Car
    template_name = 'car_management/car_details.html'
    pk_url_kwarg = 'pk'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            car = self.get_object()
            return render(request, self.template_name,{'car': car})
        return HttpResponseRedirect(reverse_lazy('login'))
    
@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class CarDetailsPageViewshop(DetailView):
    model = Car
    template_name = 'car_management/car_details.html'
    pk_url_kwarg = 'pk'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            car = self.get_object()
            return render(request, self.template_name, {'car': car})
        return HttpResponseRedirect(reverse_lazy('login'))



@login_required
def add_comment(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        comment_text = request.POST.get('comment')
        Comment.objects.create(user=request.user, car=car, name=name, comment=comment_text)
    return render(request, 'car_management/car_details.html', {'car': car})

