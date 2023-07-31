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
    # ex: /users/1/pantry/add/
    path('users/<int:pk>/pantry/add/', views.PantryRoutes.as_view(), name='pantry_add'),
    # ex: /users/1/pantry/remove/
    path('users/<int:pk>/pantry/remove/', views.PantryRoutes.as_view(), name='pantry_remove'),
    # ex: /users/1/recipes/
    path('users/<int:pk>/recipes/', views.RecipesRoutes.as_view(), name='recipes'),

]