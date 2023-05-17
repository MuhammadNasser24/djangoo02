from django.shortcuts import render
from .forms import loginform
from .models import login

# Create your views here ...

def about(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    data = login(username=username, password=password)


    return render(request,'about.html',{'lf':loginform})