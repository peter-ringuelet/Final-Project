from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='movies-page'),
    path('create/', views.blog_new, name='movie-create'),
    path('<int:pk>/', views.blog_detail, name='movie-detail'),
    path('<int:pk>/update/', views.blog_edit, name='movie-update'),
    path('<int:pk>/delete/', views.blog_delete, name='movie-delete'),
]
