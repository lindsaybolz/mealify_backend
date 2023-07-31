from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import bad_request
from rest_framework import authentication, permissions
from rest_framework import status
from django.shortcuts import render, redirect, get_object_or_404

from .models import User, Pantry, Recipe
import datetime
# session = requests.session()
# token = session.get('http://127.0.0.1:8000/rest_api/login/')

# session.post('http://127.0.0.1:8000/rest_api/login/',
#              data={
#                  'username': 'lindsayadmin',
#                  'password': 'password',
#                  'csrfmiddlewaretoken': token})

# token = session.get('http://127.0.0.1:8000/rest_api/users/')
# data = json.dumps({'test': 'value'})
# session.post('http://127.0.0.1:8000/myTestView/',
#              data={
#                  'csrfmiddlewaretoken': token,
#                  'data': data})



def validate_model(cls, model_id):
    model = cls.objects.filter(pk=model_id)

    if len(model) == 0:
        status_code = 400
        content = {'please move along': 'nothing to see here'}
        default_detail = {'test': 'test'}#f"{cls} {model_id} does not exist"
        return HttpResponseRedirect('/rest_api/users/')#f"{cl/s} {model_id} does not exist")
        # return Response(content, status=status.HTTP_400_BAD_REQUEST)

    return model


# Create your views here.
def index(request):
    return HttpResponse("Hello World")


def login(request):
    print('in login')
    return Response("Successfully logged in")
    # # print(request.POST)
    # username = request.POST['username']
    # password = request.POST['password']
    # # user = "TEST"
    # user = authentication(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     return Response(user.to_dict())
    #     HttpResponse(f'User {username} successfully loged in.')
    #     # response

    # else:
    #     # invalid response
    #     pass


def logout_view(request):
    logout(request)

class UsersRoutes(APIView):

    def get(self, request, **args):
        if args.get('pk'):
            user = get_object_or_404(User, pk=args['pk'])
            return Response(user.to_dict())
        else:   
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

class PantryRoutes(APIView):

    def post(self, request, **args):
        user = get_object_or_404(User, pk=args['pk'])
        food_list = request.data['food_list']
        new_pantry = Pantry.objects.create( 
            user = user,
            food_list = food_list,
        )
        return Response(f'New pantry successfully registered {new_pantry.to_dict()}')

