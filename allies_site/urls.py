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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
