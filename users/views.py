from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileEditForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

class CustomLoginView(LoginView):
    template_name = 'users/registration/login.html'  
    redirect_authenticated_user = True 
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/registration/signup.html'  # Custom path
    
def home(request):
    return render(request, 'users/home.html')

def profile(request):
    return render(request, 'users/profile.html')


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'users/home.html'

@login_required
def profile_edit(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm(
            request.POST, 
            request.FILES, 
            instance=request.user.profile
        )
        if profile_form.is_valid():
            profile_form.save()
            return redirect('home')
    else:
        profile_form = ProfileEditForm(instance=request.user.profile)
    
    return render(
        request,
        'users/profile_edit.html',
        {'profile_form': profile_form}
    )