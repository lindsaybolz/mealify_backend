from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions



from .models import User, Pantry, Recipe

# Create your views here.
def index(request):
    return HttpResponse("Hello World")


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    # user = "TEST"
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        HttpResponse(f'User {username} successfully loged in.')
        # response

    else:
        # invalid response
        pass


def logout_view(request):
    logout(request)

class ListUsers(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        usernames = [user.to_dict() for user in User.objects.all()]
        return Response(usernames)


    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        response = f'Successfully deleted {str(user)}'
        user.delete()
        return Response(response)


    def post(self, request):
        # Add validataion!
        new_user = User.objects.create( 
            password = request.data['password'],
            username = request.data['username'],
            first_name = request.data['first_name'],
            last_name = request.data['last_name'],
            email = request.data['email'],
            alergies = request.data['alergies'],
            restrictions = request.data['restrictions'],
            prefrences = request.data['prefrences']
        )
        return Response(f'New user successfully registered {new_user.to_dict()}')


    def patch(self, request, pk):
        # user = User.objects.get(pk=pk)
        # for key in request.data.keys():
        #     user
        pass

