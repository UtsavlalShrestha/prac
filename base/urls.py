from django.urls import path
from .import views



urlpatterns = [
    path('', views.home, name = "home"),
    path('list/', views.list, name = "list"),
    path('create/', views.create_note, name= "create_note"),
    path('choose_category/', views.choose_category, name= "choose_category"),
    path('edit_category/<int:pk>/', views.edit_category, name= "edit_category"),
    path('edit_note/<int:pk>/', views.edit_note, name= "edit_note"),
]
