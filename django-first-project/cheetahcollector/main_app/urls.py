from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('home/', views.home, name='home'),
path('about/', views.about, name='about'),
path('cheetahs/', views.cheetahs_index, name='index'),
path('cheetahs/<int:cheetah_id>/', views.cheetahs_detail, name='detail'),
path('cheetahs/create/', views.CheetahCreate.as_view(), name='cheetahs_create'),
path('cheetahs/<int:pk>/update/', views.CheetahUpdate.as_view(), name='cheetahs_update'),
path('cheetahs/<int:pk>/delete/', views.CheetahDelete.as_view(), name='cheetahs_delete'),
path('cheetahs/<int:cheetah_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]