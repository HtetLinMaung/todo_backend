from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('todo/', views.todo_list),
    path('todo/<int:pk>/', views.todo_detail),
])
