from django.urls import path

from . import views

urlpatterns = [
    # ex: /rest_api/
    path('', views.index, name='index'),
    # ex: /rest_api/login/
    path('login/', views.login, name='login'),
    # ex: /rest_api/logout/
    path('logout/', views.logout, name='logout'),
    # ex: /rest_api/users/
    path('users/', views.UsersRoutes.as_view(), name='users'),
    # ex: /rest_api/users/5
    path('users/<int:pk>', views.UsersRoutes.as_view(), name='users_id'),
    # ex: /users/1/pantry/
    path('users/<int:pk>/pantry/', views.PantryRoutes.as_view(), name='pantry'),
]