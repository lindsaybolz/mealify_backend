from django.urls import include, path
from .views import TestView

urlpatterns = [
    path('', TestView.as_view()),
]