from django.urls import path
from blogs import views

urlpatterns = [
    #url of the base by example
    #path('base', views.base, name='base'),
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('add_post', views.add_post, name='add_post'),
]