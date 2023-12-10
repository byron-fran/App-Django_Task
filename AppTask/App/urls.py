from django.urls import path
from . import views
from .models import Task
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('tareas/', views.TaskView.as_view(), name='task'),
    path('create_task/', views.TaskCreateView.as_view(), name='create_task'),
    path('detail/<int:pk>', views.TaskDetailView.as_view(), name='detail'),
    path('edit/<int:pk>', views.TaskUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', views.TaskDeleteView.as_view(), name='delete'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register', views.RegisterView.as_view(), name='register')

]