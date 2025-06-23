from django.urls import path, include
from users.views import HomeView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
] 
