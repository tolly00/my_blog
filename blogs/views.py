from django.shortcuts import render,redirect
from .models import BlogPost
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
#
def index(request):
    return render(request, 'blogs/index.html')

def post(request):
    post=BlogPost.objects.order_by('date_added')
    context={'post': post}
    return render(request, 'blogs/post.html', context)

def add_post(request):
    if request.method != 'POST':
        form= PostForm()
    else:
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('post'))
            
    context={'form':form}
    return render(request, 'blogs/add_post.html',context)

def login(request):
    return render(request, 'users/login.html')
