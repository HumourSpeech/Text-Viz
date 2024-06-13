from django.urls import path
from . import views

urlpatterns=[
    path("",views.popup, name='popup'),
]
