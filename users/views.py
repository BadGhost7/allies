from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileEditForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.views.generic import UpdateView
from django.contrib.auth import logout

from .models import UserProfile


from django.shortcuts import render, get_object_or_404
def custom_logout(request):
    logout(request)
    return redirect('/')  # Жёсткий редирект на главную


def show_profile(request, profile_id):
    """Функция для отображения профиля, как странички героя в Dota"""
    # Ищем профиль в базе. Если нет — покажет 404 (как роспись "герой мертв")
    profile = get_object_or_404(UserProfile, id=profile_id)
    
    # Рендерим HTML-шаблон и передаём туда данные профиля (как отправка данных в чат)
    return render(request, 'users/profile.html', {'profile': profile})

class CustomLoginView(LoginView):
    template_name = 'users/registration/login.html'  
    redirect_authenticated_user = True 
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/registration/signup.html'  
    
def home(request):
    return render(request, 'users/home.html')

def profile(request):
    return render(request, 'users/profile.html')





class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'users/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Ваш профиль (создаём, если не существует)
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        context['form'] = ProfileForm(instance=profile)
        
        # Анкеты других пользователей (исправленный запрос)
        context['public_profiles'] = UserProfile.objects.filter(
            is_public=True
        ).exclude(
            user=self.request.user
        ).select_related('user')  # Оптимизация
        return context
    
    def post(self, request, *args, **kwargs):
        # Обрабатываем только сохранение анкеты
        if 'save_profile' in request.POST:  # Добавьте name="save_profile" к кнопке сохранения
            profile = UserProfile.objects.get(user=request.user)
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
        return redirect('home')
   

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

class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


# Стало (исправленная версия):
def public_profiles_view(request):
    # Фильтруем ТОЛЬКО публичные анкеты (is_public=True)
    profiles = UserProfile.objects.filter(is_public=True).exclude(user=request.user)
    return render(request, 'template.html', {'profiles': profiles})

def profiles_list(request):
    """Список всех публичных анкет"""
    profiles = UserProfile.objects.filter(is_public=True).exclude(user=request.user)
    return render(request, 'users/profiles_list.html', {'profiles': profiles})

def profile_detail(request, profile_id):
    real_id = profile_id + 1  # Добавляем 1 к полученному ID
    profile = get_object_or_404(Profile, pk=real_id)
    # Дальнейшая логика
    return render(request, 'users/profile_detail.html', {'profile': profile})