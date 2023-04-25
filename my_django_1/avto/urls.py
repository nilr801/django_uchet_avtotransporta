from django.urls import path
from . import views
urlpatterns = [
    path('voditels', views.voditels_home, name = "voditels_home"),
    path('voditels_create', views.voditels_create, name = "voditels_create"),
    path('voditels/<int:pk>', views.VoditelsDetailVeiw.as_view(), name = "voditels_view"),
    path('voditels/<int:pk>/update', views.VoditelsUpdateView.as_view(), name = "voditels_update"),
    path('voditels/<int:pk>/delete', views.VoditelsDeleteView.as_view(), name = "voditels_delete"),

    path('avto', views.avto_home, name = "avto_home"),
    path('avto_create', views.avto_create, name = "avto_create"),
    path('avto/<int:pk>', views.AvtoDetailVeiw.as_view(), name = "avto_view"),
    path('avto/<int:pk>/update', views.AvtoUpdateView.as_view(), name = "avto_update"),
    path('avto/<int:pk>/delete', views.AvtoDeleteView.as_view(), name = "avto_delete"),

    path('strahovki', views.strahovki_home, name = "strahovki_home"),
    path('strahovki_create', views.strahovki_create, name = "strahovki_create"),


    path('techosmotr', views.techosmotr_home, name = "techosmotr_home"),
    path('techosmotr_create', views.techosmotr_create, name = "techosmotr_create"),

]