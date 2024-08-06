from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    #Login page
    path('login/', LoginView.as_view(), name='login'),
    
]