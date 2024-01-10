from django.urls import path, register_converter

from volkswagen.views import *

from volkswagen.views import index

urlpatterns = [
    path('', index, name='home')
]