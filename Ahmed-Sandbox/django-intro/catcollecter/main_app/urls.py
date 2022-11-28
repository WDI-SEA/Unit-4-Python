from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='cats'),

    # Cat details page
    path('cats/<int:cat_id>', views.cats_details, name='details'),

    # Class Based Views Below for Creating
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),

    # Class Based Views Below for Updating
    path('cats/<int:pk>/update', views.CatUpdate.as_view(), name='cats_update'),
    
    # Class Based Views Below for Deleting
    path('cats/<int:pk>/delete', views.CatDelete.as_view(), name='cats_delete'),


]
