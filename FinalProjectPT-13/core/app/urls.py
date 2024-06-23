from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('post_detail/<int:pk>/', views.post_detail_view, name='detail'),
    path('post_create/', views.post_create_view, name='create'),
    path('post_delete/<int:pk>/', views.post_delete_view, name='delete')
]
