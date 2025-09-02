
from django.urls import path
from . import views 

urlpatterns = [
    path('nuevo/', views.estudiante_nuevo, name='estudiante_nuevo'),
]