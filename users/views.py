from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from django.urls import reverse

# Create your views here.
# Logout the user
def logout_view(request):
    return redirect(reverse('blogs/index.html'))