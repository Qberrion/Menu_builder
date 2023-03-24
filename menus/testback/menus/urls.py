from django.urls import path
from . import views

urlpatterns = [
    path('menu/<menu_path>', views.main_menu),
    path('', views.main_index),
]
