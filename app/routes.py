from flask import Blueprint, request, jsonify, abort, make_response
from sqlalchemy.orm.attributes import flag_modified    
from app import db
from app.models.user import User
from app.models.recipe import Recipe
from app.models.pantry import Pantry
import json

# import requests 
# import os
import re


# Helper Functions:
def validate_model(model_class, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({'message': f"{model_id} is not a valid type.  It must be an integer"}, 400))

    model = model_class.query.get(model_id)

    if not model:
        abort(make_response({'message': f'{model_id} does not exist'}, 404))

    return model


users_bp = Blueprint("users", __name__, url_prefix="/users")
pantry_bp = Blueprint("pantry", __name__, url_prefix="/pantry")
recipes_bp = Blueprint("recipes", __name__, url_prefix="/recipes")
"""
USER ROUTES
"""
# create a user
@users_bp.route("/register", methods=["POST"])
def create_user():
    request_body = request.get_json()
    try:
        if request_body.get('username') and request_body.get('password') and request_body.get('email'):
            new_user = User.from_dict(request_body)
        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user.to_dict()), 201
    except:
        abort(make_response({"message": "User input data invalid.  Make sure the username and email are unique."}, 400))
    
    
@users_bp.route("/login", methods = ["POST"])
def login():    
    request_body = request.get_json()
    print('request_body["email"]: ',  request_body['email'])
    user = User.query.filter_by(email=request_body['email']).first()
    if not user:
        return 'That email is invalid', 400
    elif user.password != request_body['password']:
        return 'Invalid password', 400
    return user.to_dict(), 200


@users_bp.route("/logout", methods = ["GET"])
def logout():    
    print('logout')
    return 'Successfully logged out!', 200


@users_bp.route("", methods = ["GET"])
def get_users():
    users = User.query.all()
    users_response = []
    for user in users:
        users_response.append(user.to_dict())
    
    return jsonify(users_response), 200


@users_bp.route("/<user_id>", methods = ["GET"])
def get_one_user(user_id):
    user = validate_model(User, user_id)
    return user.to_dict(), 201


@users_bp.route("/<user_id>/alergies/add", methods=['PATCH'])
def add_user_alergies(user_id):
    user = validate_model(User, user_id)
    alergies = request.get_json()['alergies']
    new_alergies = json.loads(user.alergies)
    for alergie in alergies:
        if new_alergies.get(alergie) == None:    
            new_alergies[alergie] = 1

    user.alergies = new_alergies
    db.session.commit()
    return user.to_dict(), 200


@users_bp.route("/<user_id>/alergies/remove", methods=['PATCH'])
def remove_user_alergies(user_id):
    user = validate_model(User, user_id)
    alergies = request.get_json()['alergies']
    new_alergies = json.loads(user.alergies)
    for alergie in alergies:
        if new_alergies.get(alergie):    
            new_alergies.pop(alergie)
        else:
            return f"{alergie} is not in the existing alergies", 400

    user.alergies = new_alergies
    db.session.commit()
    return user.to_dict(), 200


@users_bp.route("/<user_id>/prefrences/add", methods=['PATCH'])
def add_user_prefrences(user_id):
    user = validate_model(User, user_id)
    prefrences = request.get_json()['prefrences']
    new_prefrences = json.loads(user.prefrences)
    for prefrence in prefrences:
        if new_prefrences.get(prefrence) == None:    
            new_prefrences[prefrence] = 1

    user.prefrences = new_prefrences
    db.session.commit()
    return user.to_dict(), 200


@users_bp.route("/<user_id>/prefrences/remove", methods=['PATCH'])
def remove_user_prefrences(user_id):
    user = validate_model(User, user_id)
    prefrences = request.get_json()['prefrences']
    new_prefrences = json.loads(user.prefrences)
    for prefrence in prefrences:
        if new_prefrences.get(prefrence):    
            new_prefrences.pop(prefrence)
        else:
            return f"{prefrence} is not in the existing prefrences", 400

    user.prefrences = new_prefrences
    db.session.commit()
    return user.to_dict(), 200


@users_bp.route("/<user_id>/restrictions/add", methods=['PATCH'])
def add_user_restrictions(user_id):
    user = validate_model(User, user_id)
    restrictions = request.get_json()['restrictions']
    new_restrictions = json.loads(user.restrictions)
    for restriction in restrictions:
        if new_restrictions.get(restriction) == None:    
            new_restrictions[restriction] = 1

    user.restrictions = new_restrictions
    db.session.commit()
    return user.to_dict(), 200


@users_bp.route("/<user_id>/restrictions/remove", methods=['PATCH'])
def remove_user_restrictions(user_id):
    user = validate_model(User, user_id)
    restrictions = request.get_json()['restrictions']
    new_restrictions = json.loads(user.restrictions)
    for restriction in restrictions:
        if new_restrictions.get(restriction):    
            new_restrictions.pop(restriction)
        else:
            return f"{restriction} is not in the existing restrictions", 400

    user.restrictions = new_restrictions
    db.session.commit()
    return user.to_dict(), 200


@users_bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = validate_model(User, user_id)

    db.session.delete(user)
    db.session.commit()

    return jsonify(f'User {user_id} successfully deleted'), 201


"""
PANTRY ROUTES
"""
@users_bp.route('/<user_id>/pantry', methods=['POST'])
def create_pantry_for_user(user_id):
    user = validate_model(User, user_id)
    if list(Pantry.query.filter_by(user=user)) == []:
        request_body = request.get_json()
        food_dict = {}
        for item in request_body['food_list']:
            food_dict[item] = 1
        pantry_dict = {
            'user': user,
            'user_id': user_id,
            'food_dict': food_dict,
        }

        new_pantry = Pantry.from_dict(pantry_dict)
        db.session.add(new_pantry)
        db.session.commit()

        return new_pantry.to_dict(), 200
    else:
        return f'User with id={user_id} already has a pantry', 400


@users_bp.route('/<user_id>/pantry', methods=['GET'])
def get_pantry_for_user(user_id):
    user = validate_model(User, user_id)
    pantry = Pantry.query.filter_by(user=user)
    if list(pantry) == []:
        return jsonify([]), 200

    return list(pantry)[0].to_dict(), 200


@pantry_bp.route('/<pantry_id>/add', methods=['PATCH'])
def add_items_to_pantry(pantry_id):
    pantry = validate_model(Pantry, pantry_id)
    new_items = request.get_json()['food_list']
    new_food_dict = pantry.food_dict
    for item in new_items:
        if pantry.food_dict.get(item) == None:    
            new_food_dict[item] = 1
            flag_modified(pantry, 'food_dict')


    pantry.food_dict = new_food_dict
    db.session.commit()
    return pantry.to_dict(), 200


@pantry_bp.route('/<pantry_id>/remove', methods=['PATCH'])
def remove_items_to_pantry(pantry_id):
    pantry = validate_model(Pantry, pantry_id)
    new_items = request.get_json()['food_list']
    for item in new_items:
        if pantry.food_dict.get(item):    
            pantry.food_dict.pop(item)
            flag_modified(pantry, 'food_dict')
        else:
            return f'{item} is not in the pantry', 400

    db.session.commit()
    return pantry.to_dict(), 200


@pantry_bp.route('/<pantry_id>', methods=['DELETE'])
def delete_pantry(pantry_id):
    pantry = validate_model(Pantry, pantry_id)

    db.session.delete(pantry)
    db.session.commit()

    return jsonify(f'Pantry {pantry_id} successfully deleted'), 201


"""
RECIPE ROUTES
"""

@users_bp.route('/<user_id>/recipes', methods=['POST'])
def create_recipe_for_user(user_id):
    user = validate_model(User, user_id)
    request_body = request.get_json()
    ingredients = {}
    for ingredient in request_body['ingredients']:
        ingredients[ingredient] = 1
        
    recipe_dict = {
        'user': user,
        'user_id': user_id,
        'title': request_body['title'],
        'ingredients': ingredients,
        'nutritional_data': request_body['nutritional_data'],
        'url': request_body['url'],
        'user_state': request_body['user_state'],
        'instructions': request_body['instructions'],
    }
    new_recipe = Recipe.from_dict(recipe_dict)
    db.session.add(new_recipe)
    db.session.commit()
    return new_recipe.to_dict(), 200

@users_bp.route('/<user_id>/recipes', methods=['GET'])
def get_recipe_for_user(user_id):
    print('in get_recipes')
    user = validate_model(User, user_id)
    recipes = Recipe.query.filter_by(user=user)
    pantry_query = request.args.getlist("pantry")
    ingredient_query = request.args.getlist("ingredients")
    filtered_recipes = []
    print(pantry_query)
    if not ingredient_query and not pantry_query:
        for recipe in recipes:
            if recipe.user_state != -1:
                filtered_recipes.append(recipe.to_dict())
        print('no queies')

        return jsonify(filtered_recipes), 200
    
    else:
        if pantry_query:
            pantry = Pantry.query.filter_by(user=user).first()
            pantry_ingredients = pantry.food_dict
            for ingredient in pantry_ingredients.keys():
                for recipe in recipes:  
                    recipe_ingredients = json.loads(recipe.ingredients.replace("'", '"'))
                    if recipe_ingredients.get(ingredient):
                        filtered_recipes.append(recipe.to_dict())
        if ingredient_query:
            for ingredient in ingredient_query[0].split(', '):
                for recipe in recipes:
                    recipe_ingredients = json.loads(recipe.ingredients.replace("'", '"'))
                    if recipe_ingredients.get(ingredient):
                        filtered_recipes.append(recipe.to_dict())
        if filtered_recipes == []:
            return 'No recipes matching these requirements are saved to this user profile.', 200
        else:
            return jsonify(filtered_recipes), 200

@recipes_bp.route('/<recipe_id>/favorite', methods=['PATCH'])
def favorite_recipe(recipe_id):
    recipe = validate_model(Recipe, recipe_id)
    recipe.user_state = 1

    db.session.commit()
    return jsonify(recipe.to_dict()), 200


@recipes_bp.route('/<recipe_id>/unfavorite', methods=['PATCH'])
def unfavorite_recipe(recipe_id):
    recipe = validate_model(Recipe, recipe_id)
    recipe.user_state = -1

    db.session.commit()
    return jsonify(recipe.to_dict()), 200


@recipes_bp.route('/<recipe_id>/neutralize', methods=['PATCH'])
def neutralize_recipe(recipe_id):
    recipe = validate_model(Recipe, recipe_id)
    recipe.user_state = 0

    db.session.commit()
    return jsonify(recipe.to_dict()), 200


@recipes_bp.route('/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = validate_model(Recipe, recipe_id)

    db.session.delete(recipe)
    db.session.commit()

    return jsonify(f'Recipe {recipe_id} successfully deleted'), 201

