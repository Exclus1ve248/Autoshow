from django.urls import path, register_converter

from volkswagen.views import *

from volkswagen.views import index

urlpatterns = [
    path('', index, name='home'),
    path('organization/', org, name='org'),
    path('automobile/', auto, name='auto'),
    path('about/', about, name='about'),
    path('automobile/add_eq/', add_eq, name='add_eq'),
    path('automobile/add_serv/', add_serv, name='add_serv'),
    path('form1/', clients1Form, name='form1')
]