from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('about/',views.about ),
    path('cats/', views.cats_index, name='index'),
    # path('contact',views.contact ) 
    # Cat Details Page
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    # new route used to show a form and create a cat
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
    path('cats/<int:pk>/delete/',views.CatDelete.as_view(), name='cats_delete'),
    path('cats/<int:pk>/update/',views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name="add_feeding")
]