from django.shortcuts import render,redirect
from .models import BlogPost
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
#
def index(request):
    return render(request, 'blogs/index.html')

@login_required
def post(request):
    post=BlogPost.objects.filter(owner=request.user).order_by('date_added')
    context={'post': post}
    return render(request, 'blogs/post.html', context)

@login_required
def add_post(request):
    if request.method != 'POST':
        form= PostForm()
    else:
        form=PostForm(request.POST)
        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.owner=request.user
            new_post.save()
            form.save()
            return HttpResponseRedirect(reverse('post'))
            
    context={'form':form}
    return render(request, 'blogs/add_post.html',context)


