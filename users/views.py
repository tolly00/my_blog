from django.shortcuts import redirect,render
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

# Create your views here.
# Logout the user
def logout_view(request):
    return redirect(reverse('blogs/index.html'))

def register_view(request):
    #register a new user
    if request.method != 'POST':
        #display blank registration form.
        form=UserCreationForm()
    else:
        #process complete form
        form= UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user=form.save()
            #log the user and redirect to home page
            authenticated_user=authenticate(username=new_user.username,password=request.POST['password1'])
            LoginView.as_view(request,authenticated_user)
            return HttpResponseRedirect(reverse('index'))
        
    context={'form':form}
    return render(request, 'registration/register.html', context)
            