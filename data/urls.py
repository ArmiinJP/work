from django.urls import path

from data import views

urlpatterns = [
    path('create/', views.create_base_dataset),
    path('delete/', views.delete_base_dataset),
    path('select/', views.select_sql),
    path('alter/', views.alter_sql),
]
