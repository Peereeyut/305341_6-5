#urls.py

from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', list_view, name='home-list'),

]