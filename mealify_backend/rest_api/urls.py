from django.urls import path

from . import views

urlpatterns = [
    # ex: /rest_api/
    path('', views.index, name='index'),
    # ex: /rest_api/login/
    path('login/', views.login, name='login'),
    # ex: /rest_api/logout/
    path('logout/', views.logout, name='logout')
]