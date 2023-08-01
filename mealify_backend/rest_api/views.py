from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout

from .models import User, Pantry, Recipe

# Create your views here.
def index(request):
    return HttpResponse("Hello World")


# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     # user = "TEST"
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         HttpResponse(f'User {username} successfully loged in.')
#         # response

#     else:
#         # invalid response
#         pass


def logout_view(request):
    logout(request)

class UserListView(ListView):
    model = User

    def get(self, request):
        pass


    def delete(self, request):
        pass


    def post(self, request):
        pass


    def patch(self, request):
        pass
