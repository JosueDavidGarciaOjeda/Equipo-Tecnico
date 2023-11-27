from django.shortcuts import render
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login 
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import RegisterFrom
from django.contrib.auth.models import User

def index(request):
    return render(request,'Garantia1.html',{
        'message': 'Nuevo mensaje desde la vista',
        'products':[
            {'title:':'Casio','price':7,'stock':True},
            {'title:':'Rolroyce','price':25,'stock':True},
            {'title:':'Rolex','price':154,'stock':False},
        ]
    } )
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)#none
        if user:
            login(request, user)
            messages.success(request,'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request,'Usuario o Contraseña no validos {}')
            
            
    return render(request, 'users/login.html',{
        
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login'),

def register(request):
    form = RegisterFrom(request.POST or None)
    
    if request.method =='POST' and form.is_valid():
        
        user = form.save() 
        
        if user:
            login(request, user)
            messages.success(request, 'Usuario Creado exitosamente')
            return redirect('index')
            
            
    return render(request,'users/register.html',{
        'form':form
    })

