from django.urls import path 
from . import views

urlpatterns= [
  path('todos/',views.todo_list,name='todos'),
  path('todos/todo-details/<int:pk>',views.todo_details,name='todo-details'),
]