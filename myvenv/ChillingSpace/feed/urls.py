from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name = 'home_view'),
    path('<int:post_id>/', views.post_view, name='post_view'),
]
