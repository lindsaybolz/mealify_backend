from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication

from user_api.models import AppUser
# from .models import User, Pantry, Recipe
from .models import Pantry, Recipe

# Create your views here.
class LoginView(APIView):
    def get(self, request):
        return Response("Successfully logged in")


class LogoutView(APIView):
    def get(self, request):
        return Response('Successfully logged out')


class UsersRoutes(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request, **args):
        if args.get('pk'):
            user = get_object_or_404(AppUser, pk=args['pk'])
            return Response(user.to_dict())
        else:   
            usernames = [user.to_dict() for user in AppUser.objects.all()]
            return Response(usernames)


    def delete(self, request, pk):
        user = AppUser.objects.get(pk=pk)
        response = f'Successfully deleted {str(user)}'
        user.delete()
        return Response(response)


    # def post(self, request):

    #     # Add validataion!
    #     new_user = AppUser.objects.create( 
    #         password = request.data['password'],
    #         username = request.data['username'],
    #         first_name = request.data['first_name'],
    #         last_name = request.data['last_name'],
    #         email = request.data['email'],
    #         alergies = request.data['alergies'],
    #         restrictions = request.data['restrictions'],
    #         prefrences = request.data['prefrences']
    #     )
    #     return Response(new_user.to_dict())


class PantryRoutes(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request, **args):
        pantry = get_object_or_404(Pantry, user_id=args['pk'])
        return Response(pantry.to_dict())

    def post(self, request, **args):
        user = get_object_or_404(AppUser, pk=args['pk'])
        food_list = {}
        for item in request.data['food_list']:
            food_list[item] = 1
        # food_list = request.data['food_list']
        new_pantry = Pantry.objects.create( 
            user = user,
            food_list = food_list,
        )
        return Response(new_pantry.to_dict())

    def patch(self, request, **args):
        path = request.META.get('PATH_INFO', None).split('/')[-2]
        pantry = get_object_or_404(Pantry, user_id=args['pk'])
        new_items = request.data['food_list']
        if path == 'add':
            for item in new_items:
                pantry.food_list[item] = 1
            pantry.save()
            return Response(pantry.to_dict())
        elif path == 'remove':
            for item in new_items:
                pantry.food_list.pop(item)
            pantry.save()
            return Response(pantry.to_dict())

    def delete(self, request, **args):
        pantry = get_object_or_404(Pantry, user_id=args['pk'])
        pantry_dict = pantry.to_dict()
        pantry.delete()
        return Response(f'Pantry successflly deleted: id = {pk}')

class RecipesRoutes(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)


    def post(self, request, **args):
        user = get_object_or_404(AppUser, pk=args['pk'])
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
        return Response(new_recipe.to_dict())

    def get(self, request, **args):        
        recipes = get_list_or_404(Recipe, user_id=args['pk'])
        if len(request.GET.keys()) == 0:
            recipes_response = []
            for recipe in recipes:
                recipes_response.append(recipe.to_dict())

            return Response(recipes_response)
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
                return Response(filtered_recipes)

    def patch(self, request, **args):
        path = request.META.get('PATH_INFO', None).split('/')[-2]
        recipe = get_object_or_404(Recipe, pk=args['pk'])

        if path == 'favorite':
            recipe.user_state = 1
        elif path == 'unfavorite':
            recipe.user_state = -1
        elif path == 'neutralize':
            recipe.user_state = 0

        recipe.save()
        return Response(recipe.to_dict())

