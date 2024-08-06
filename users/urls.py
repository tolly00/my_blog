from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    #Login page
    path('login/', LoginView.as_view(), name='login'),
    #path('logout/', views.logout_view, name='logout'),
     path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    
]