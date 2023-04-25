from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Voditels
from .forms import VoditelsForm
from .models import Cars
from .forms import CarsForm
from .models import Strahovki
from .forms import StrahovkiForm
from .models import Techosmotr
from .forms import TechosmotrForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.core.exceptions import ValidationError
from django.contrib.auth.views import LoginView

from django.contrib.auth.models import User


# Create your views here.
def voditels_home(request):
    voditels = Voditels.objects.all()
    return render(request, 'avto/avto_voditels_home.html', {'voditels':voditels})

def voditels_create(request):
    error = ''
    if request.method == "POST":
        form = VoditelsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена не правильно'

    form = VoditelsForm()

    data = {'form': form, 'error': error}

    return render(request, 'avto/avto_vodit_create.html', data)

class VoditelsDetailVeiw(DetailView):
    model = Voditels
    template_name = 'avto/voditels_details_view.html'
    context_object_name = 'voditel'

class VoditelsUpdateView(UpdateView):
    model = Voditels
    template_name = 'avto/avto_vodit_create.html'

    form_class = VoditelsForm

class VoditelsDeleteView(DeleteView):
    model = Voditels
    success_url = '/avto/voditels'
    template_name = 'avto/voditels_delete.html'



def avto_home(request):
    avto = Cars.objects.all()
    return render(request, 'avto/avto_car_home.html', {'avto':avto})
def avto_create(request):
    def validate_unique(value):
        if Cars.objects.filter(voditels=value).exists():
            raise ValidationError('This value must be unique.')
    def validate_unique_vin(value):
        if Cars.objects.filter(vin_number=value).exists():
            raise ValidationError('This value must be unique.')


    error = ''
    if request.method == "POST":


        form = CarsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена не правильно'

    form = CarsForm()

    data = {'form': form, 'error': error}

    return render(request, 'avto/avto_car_create.html', data)




class AvtoDetailVeiw(DetailView):
    model = Cars
    template_name = 'avto/avto_details_view.html'
    context_object_name = 'car'

class AvtoUpdateView(UpdateView):
    model = Cars
    template_name = 'avto/avto_car_create.html'
    form_class = CarsForm

class AvtoDeleteView(DeleteView):
    model = Cars
    success_url = '/avto/avto'
    template_name = 'avto/avto_delete.html'




def strahovki_home(request):
    strahovki = Strahovki.objects.all()
    return render(request, 'avto/avto_strahovki_home.html', {'strahovki':strahovki})

def strahovki_create(request):
    error = ''
    if request.method == "POST":
        form = StrahovkiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена не правильно'

    form = StrahovkiForm()

    data = {'form': form, 'error': error}

    return render(request, 'avto/avto_strahovki_create.html', data)






def techosmotr_home(request):
    techosmotr = Techosmotr.objects.all()
    return render(request, 'avto/avto_techosmotr_home.html', {'techosmotr':techosmotr})


def techosmotr_create(request):
    error = ''
    if request.method == "POST":
        form = TechosmotrForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
           error = 'Форма заполнена не правильно'

    form = TechosmotrForm()
    data = {'form': form, 'error': error}

    return render(request, 'avto/avto_techosmotr_create.html', data)





