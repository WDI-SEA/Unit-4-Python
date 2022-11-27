from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='cats'),
    path('cats/<int:cat_id>', views.cats_details, name='details')
]
