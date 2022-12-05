from django.urls import path
from . import views

urlpatterns = [
    # the path would be /home
    path('home/', views.home),
    path('about/', views.about),
    path('cats/', views.cats_index, name='index'),
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    # classes are written in camel case
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
    # when we work with classes we use pk & when we work with functions we use _id
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding')
]
