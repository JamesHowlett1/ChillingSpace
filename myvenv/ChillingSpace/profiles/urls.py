from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name = 'home_view'),
    path('my_profile/',views.my_profile_view, name='my_profile_view'),
    path('<int:profile_id>/', views.profile_view, name='profile_view'),
]
