from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import bad_request
from rest_framework import authentication, permissions
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404

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


class LoginView(APIView):

    def get(self, request):
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


class LogoutView(APIView):
    def get(self, request):
        return Response('Successfully logged out')

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

    def get(self, request, **args):
        pantry = get_object_or_404(Pantry, user_id=args['pk'])
        return Response(f'{pantry.to_dict()}')

    def post(self, request, **args):
        user = get_object_or_404(User, pk=args['pk'])
        food_list = {}
        for item in request.data['food_list']:
            food_list[item] = 1
        # food_list = request.data['food_list']
        new_pantry = Pantry.objects.create( 
            user = user,
            food_list = food_list,
        )
        return Response(f'New pantry successfully registered {new_pantry.to_dict()}')

    def patch(self, request, **args):
        path = request.META.get('PATH_INFO', None).split('/')[-2]
        pantry = get_object_or_404(Pantry, user_id=args['pk'])
        new_items = request.data['food_list']
        if path == 'add':
            for item in new_items:
                pantry.food_list[item] = 1
            pantry.save()
            return Response(f'Pantry successfully added foods: {pantry.to_dict()}')
        elif path == 'remove':
            for item in new_items:
                print(pantry.food_list)
                pantry.food_list.pop(item)
            pantry.save()
            return Response(f'Pantry successfully deleted foods: {pantry.to_dict()}')

    def delete(self, request, **args):
        pantry = get_object_or_404(Pantry, user_id=args['pk'])
        pantry_dict = pantry.to_dict()
        pantry.delete()
        return Response(f'Pantry successflly deleted: {pantry.to_dict()}')

class RecipesRoutes(APIView):


    def post(self, request, **args):
        user = get_object_or_404(User, pk=args['pk'])
        ingredients = {}
        for ingredient in request.data['ingredients']:
            ingredients[ingredient] = 1

        new_recipe = Recipe.objects.create( 
            user = user,
            name = request.data['name'],
            ingredients = ingredients,
            instructions = request.data['instructions'],
            nutritional_data = request.data['nutritional_data'],
            url = request.data['url'],
            user_state = request.data['user_state'],
        )
        return Response(f'New recipe successfully created {new_recipe.to_dict()}')

    def get(self, request, **args):        
        recipes = get_list_or_404(Recipe, user_id=args['pk'])
        if len(request.GET.keys()) == 0:
            recipes_response = []
            for recipe in recipes:
                recipes_response.append(recipe.to_dict())

            return Response(f'{recipes_response}')
        else:
            if request.GET['pantry'] != None:
                pantry = get_object_or_404(Pantry, user_id=args['pk'])
                filtered_recipes = []
                for ingredient in pantry.food_list.keys():
                    for recipe in recipes:
                        if recipe.ingredients.get(ingredient):
                            filtered_recipes.append(recipe.to_dict())
            elif request.GET['ingredients'] != None:
                for ingredient in request.GET['ingredients'].split(', '):
                    filtered_recipes = [recipe.to_dict() for recipe in recipes if recipe.ingredients.get(ingredient) != None]
            
            if filtered_recipes == []:
                return Response('No recipes matching these requirements are saved to this user profile.')
            else:
                return Response(f'{filtered_recipes}')

    def patch(self, request, **args):
        print('in patch')
        path = request.META.get('PATH_INFO', None).split('/')[-2]
        print(args['pk'])
        recipe = get_object_or_404(Recipe, pk=args['pk'])
        print(recipe)
        if path == 'favorite':
            print('in favorite')
            recipe.user_state = 1
        elif path == 'unfavorite':
            recipe.user_state = -1
        elif path == 'neutralize':
            recipe.user_state = 0

        recipe.save()
        print(recipe.to_dict())
        return Response(f'Recipe successfully updated user state: {recipe.to_dict()}')

