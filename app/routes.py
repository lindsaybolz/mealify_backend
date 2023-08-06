from flask import Blueprint, request, jsonify, abort, make_response
from app import db
from app.models.user import User
from app.models.recipe import Recipe
from app.models.pantry import Pantry
import json

# import requests 
# import os
# import re


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
            # clean_data = validate_data(request_body)
            new_user = User.from_dict(request_body)
        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user.to_dict()), 201
    except:
        abort(make_response({"message": "User input data incomplete"}, 400))
    
    
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


@users_bp.route("/login", methods = ["GET"])
def login():    
    request_body = request.get_json()
    user = User.query.filter_by(email=request_body['email']).first()
    if not user:
        return 'That email is invalid', 400
    elif user.password != request_body['password']:
        return 'invalid password', 400
    return user.to_dict(), 200


@users_bp.route("/logout", methods = ["GET"])
def logout():    
    print('logout')
    return 'Successfully logged out!', 200



@users_bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = validate_model(User, user_id)

    db.session.delete(user)
    db.session.commit()

    return jsonify('User successfully deleted'), 201

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
    print(user.to_dict())
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
    user = validate_model(User, user_id)
    recipes = Recipe.query.filter_by(user=user)
    # print(type(request.args.getlist('ingredients')))
    pantry_query = request.args.getlist("pantry")
    ingredient_query = request.args.getlist("ingredients")
    if not ingredient_query and not pantry_query:
        recipe_response = []
        for recipe in recipes:
            if recipe.user_state != -1:
                recipe_response.append(recipe.to_dict())

        return jsonify(recipe_response), 200

    # filtered_recipes = []
    # if pantry_query:
    #     pantry = Pantry.query.filter_by(user=user)
    #     for ingredient in pantry.food_list.keys():
    #         for recipe in recipes:  
    #             if recipe.ingredients.get(ingredient):
    else:
        if ingredient_query:
            filtered_recipes = []
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

