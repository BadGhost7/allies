from django.urls import path
from main.views import index, IndexView
urlpatterns = [
    path("", index, name="index"),
    path("", IndexView.as_view(), name="IndexView")

]