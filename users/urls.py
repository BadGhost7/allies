from django.urls import path, include
from users.views import HomeView
from . import views  # Импортируем наши "скиллы" (views)
app_name = 'users'  # Добавлено пространство имен

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('profile/<int:profile_id>/', views.profile_detail, name='profile_detail'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('profiles/', views.profiles_list, name='profiles_list'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]
