from django.contrib import admin
from django.urls import path, include
from main.views import IndexView
from users import views
from django.contrib.auth import views as auth_views  
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView
from users.views import CustomLoginView
from users.views import HomeView, profile_edit
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from users.views import ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/registration/login.html'), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(
    template_name='users/registration/login.html',
    redirect_authenticated_user=True,
    success_url='home'  
), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
