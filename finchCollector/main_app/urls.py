from django.urls import path
from . import views

urlpatterns = [
  path('home', views.home, name='home'),
  path('about', views.about),
  path('index', views.finches_index),
  path('create',views.CatCreate.as_view(),name='cats_create'),
  path('<int:pk>/update',views.CatUpdate.as_view(),name='cats_update'),
  path('<int:pk>/delete',views.CatDelete.as_view(),name='cats_delete'),
  path('<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),


]