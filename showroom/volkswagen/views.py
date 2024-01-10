from django.shortcuts import render
from .models import AUTOMOBILE
from django.http import HttpResponse
# Create your views here.


# request, 'main/index.html', {'auto':auto}
menu =[{'title': 'Главная', 'url': 'home'},
       {'title': 'Организации', 'url': 'org'}
       ]
def index(request):
     data = {'title': 'Главная страница',
             'menu': menu,

             }
     return render(request, 'volkswagen/index.html', {'data':data})
# def index(request):
#      auto = AUTOMOBILE.objects.all()
#      return render(request, 'volkswagen/index.html', {'auto':auto})
