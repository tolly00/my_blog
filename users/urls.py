from django.urls import path
from blogs import views

urlpatterns = [
    #Login page
    path('login/', views.login, name='login'),
    
]