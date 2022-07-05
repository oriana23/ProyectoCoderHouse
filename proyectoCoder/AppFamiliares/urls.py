from django.urls import path
from .views import *

urlpatterns = [
    path('mama/', mama),
    path('hermano/', hermano_mayor),
    path('esposo/', esposo),
    path('bienvenida/', bienvenida),
    

    
    
    
]