from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
#from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')


# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username, password)
#             if user:
#                 auth.login(request, user)
#                 return render(request, 'main/about.html')
#     context = {'form': UserLoginForm()}
#     return render(request, 'main/login.html', context)
#
# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'main/about.html')
#     else:
#         form = UserRegistrationForm()
#     context = {'form': form}
#     return render(request, 'main/registration.html', context)



def register(request):
    if request.method == 'POST':
        # Получаем данные из POST-запроса
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Проверяем, что пароли совпадают
        if password == confirm_password:


            try:
                User.objects.create_user(username=username, email=email, password=password)
                return redirect('login')
            except:
                error_msg = 'Имя пользователя уже занято'
                return render(request, 'registration/register.html', {'error_msg': error_msg})




            # Создаем нового пользователя
            user = User.objects.create_user(username=username, email=email, password=password)

            # Авторизуем пользователя
            login(request, user)

            # Перенаправляем пользователя на главную страницу
            return redirect('home')
        else:
            # Если пароли не совпадают, показываем ошибку
            error = "Пароли не совпадают"
            return render(request, 'registration/register.html', {'error': error})

    # Если метод запроса GET, показываем страницу регистрации
    else:
        return render(request, 'registration/register.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "Неправильное имя пользователя или пароль. Попробуйте снова."
            return render(request, 'registration/login.html', {'error': error})
    return render(request, 'registration/login.html')
