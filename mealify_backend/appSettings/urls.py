from django.urls import include, path
from .views import SettingsViewView

urlpatterns = [
    path('settings', SettingsView.as_view()),
]