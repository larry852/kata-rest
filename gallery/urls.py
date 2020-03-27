from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addUser/', views.add_user_view, name='addUser'),
    path('<int:user_id>/public', views.show_public_images_user, name='showPublic'),
    path('login/', views.login, name='login')
]
