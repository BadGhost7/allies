from django.contrib import admin
from django.urls import path, include
from main.views import IndexView
from users import views
from django.contrib.auth import views as auth_views  
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView
from users.views import CustomLoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
