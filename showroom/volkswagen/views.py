from django.shortcuts import render, redirect
from .models import AUTOMOBILE, ORGANIZATION, ADD_EQUIP, ADD_SERV, clients1
from .forms import сlients1Form
from django.http import HttpResponse, HttpResponseNotFound



# request, 'main/index.html', {'auto':auto}
menu =[{'title': 'Главная', 'url': 'home'},
       {'title': 'Организации', 'url': 'org'}
       ]
def index(request):
     data = {'title': 'Главная страница',
             'menu': menu
             }
     return render(request, 'volkswagen/index.html', data)

def org(request):
    data = {'title': 'Главная страница',
            'menu': menu
            }
    org1 = ORGANIZATION.objects.all()[0]
    org2 = ORGANIZATION.objects.all()[1]

    return render(request, 'volkswagen/org.html', {'org1':org1, 'org2':org2})

def auto(request):
     auto1 = AUTOMOBILE.objects.all()[1]
     auto2 = AUTOMOBILE.objects.all()[0]
     auto3 = AUTOMOBILE.objects.all()[2]
     return render(request, 'volkswagen/auto.html', {'auto1':auto1,'auto2':auto2,'auto3':auto3})

def about(request):

    return render(request, 'volkswagen/about.html')

def add_eq(request):
    add_eq = ADD_EQUIP.objects.all()
    return render(request, 'volkswagen/add_eq.html', {'add_eq': add_eq})

def add_serv(request):
    add_serv = ADD_SERV.objects.all()
    return render(request, 'volkswagen/add_serv.html', {'add_serv': add_serv})

def clients1Form(request):
    error = ''
    if request.method == 'POST':
        form = сlients1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = сlients1Form()
    return render(request, 'volkswagen/form1.html', {'form':form})
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')

def Http404(request):
    raise Http404()
