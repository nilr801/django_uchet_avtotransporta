

from .models import Voditels
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, DateInput, Textarea
from .models import Strahovki
from .models import Cars
from .models import Techosmotr


class VoditelsForm(ModelForm):
    class Meta:
        model =Voditels
        fields = ["fio", "number_prav", "conec_prav", "primechanie"]
        widgets ={
            "fio": TextInput(attrs={'class': 'form-control', 'placeholder':"ФИО"}),
            "number_prav": TextInput(attrs={'class': 'form-control', 'placeholder': "номер прав"}),
            "conec_prav": DateInput(attrs={'class':'form-control', 'placeholder': "дата окончания прав", 'type':'date'}),
            "primechanie" :Textarea(attrs={'class':'form-control','placeholder': "примечание" })
        }

class CarsForm(ModelForm):
    class Meta:
        model = Cars
        fields = ["marka", "model", "data_vypuska", "vin_number", "number_avto", "probeg", "voditels"]
        widgets ={
            "marka": TextInput(attrs={'class': 'form-control', 'placeholder':"марка"}),
            "model": TextInput(attrs={'class': 'form-control', 'placeholder': "модель"}),
            "data_vypuska": DateInput(attrs={'class':'form-control', 'placeholder': "дата выпуска", 'type':'date'}),
            "vin_number": TextInput(attrs={'class': 'form-control', 'placeholder': "вин-номер"}),
            "number_avto": TextInput(attrs={'class': 'form-control', 'placeholder': "номер авто"}),
            "probeg" :Textarea(attrs={'class':'form-control','placeholder': "пробег" })
        }



class StrahovkiForm(ModelForm):
    class Meta:
        model = Strahovki
        fields = ["cars",
                  "sobstvennik_avto","data_nachala", "data_conca", "number_polisa"]
        widgets ={
            "sobstvennik_avto":TextInput(attrs={'class': 'form-control', 'placeholder': "собственник авто"}),
            "data_nachala": DateInput(attrs={'class': 'form-control', 'placeholder': "дата начала", 'type':'date'}),
            "data_conca": DateInput(attrs={'class': 'form-control', 'placeholder': "дата конца", 'type':'date'}),
            "number_polisa": TextInput(attrs={'class': 'form-control', 'placeholder': "номер полиса"})
        }

        def clean(self):
            if Strahovki.objects.filter(umber_polisa=self.number_polisa).exists():
                raise ValidationError("Значение поля 'my_field' должно быть уникальным.")


class TechosmotrForm(ModelForm):

    class Meta:
        model = Techosmotr
        fields = ["cars",
                  "zakazchik","data_vydachi", "srok_deistviya", "number_tex_karty"]
        widgets ={
            "zakazchik":TextInput(attrs={'class': 'form-control', 'placeholder': "заказчик ТО"}),
            "data_vydachi": DateInput(attrs={'class': 'form-control', 'placeholder': "дата пвыдачи", 'type':'date'}),
            "srok_deistviya": DateInput(attrs={'class': 'form-control', 'placeholder': "срок действия", 'type':'date'}),
            "number_tex_karty": TextInput(attrs={'class': 'form-control', 'placeholder': "номер техкарты"})
        }







