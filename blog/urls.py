from django.urls import path
from . import views

urlpatterns = [
    path('laptop/', views.laptop),
    path('refrigeradora/', views.refrigeradora),
    path('blog/', views.index),
    path('blog/crear', views.crearblog),
]
