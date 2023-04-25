from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name = "home"),
    path('about-us', views.about, name = "about"),
    path('register/', views.register, name="register"),
path('login/', views.login_view, name="login")
# path('login', views.login, name = "login"),
# path('registration', views.registration, name = "registration")
]