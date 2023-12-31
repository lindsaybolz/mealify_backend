# mealify_backend
Lindsay Wilson, Elaine Watkins, and Pha'lesa Patton Ada C19 Capstone Mealify

## Quick Start

1. Clone this repository. **You do not need to fork it first.**
    - `git clone https://github.com/lindsaybolz/mealify_backend.git`

1. Create and activate a virtual environment
    - `python3 -m venv venv`
    - `source venv/bin/activate`
1. Install the `requirements.txt`
    - `pip install -r requirements.txt`

1. Create development and testing databases in postgres
    ```
    $ psql -U postgres

    postgres=# CREATE DATABASE mealify_db;
    postgres=# CREATE DATABASE mealify_test_db;
    ```

2. Create a `.env` file with your database connection strings
    ```bash
    # .env
    # Development db connection string
    SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/mealify_db
    
    # Test db connection string
    SQLALCHEMY_TEST_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/mealify_test_db
    
    # Render db connection string
    RENDER_DATABASE_URI=postgresql+psycopg2://mealify_db_user:G5hxTc41t9hCrmK0sW3gasZ6Ml2ifDLo@dpg-cj85fq5jeehc73a7v9n0-a.oregon-postgres.render.com/mealify_db
    ```

3. Run the flask server from  `mealify_backend` directory
    ```
    $ flask run
    ```

## Endpoints
Please note there is currently zero protection for user information so use with data you are comfortable being public.
| Route | Query Parameter(s) | Route Description | Response |
|--|--|--|--|
|`POST`<br> `users/register/`| `{"email": "example@example.com", "username": "example", "password": "example123"}` | Creates a new user| `{"intolerances": "{}", "email": "example@example.com", "id": 1, "ingredient_prefrences": "{}", "recipes": [], "diet_restrictions": "{}", "username": "example"}` |
|`GET`<br> `users/login/`| `{"email": "test@example.com", "password": "testing123"}` | Simple login that does not do any real authentication.| `{"intolerances": "{}", "email": "test1@gmail.com", "id": 1, "ingredient_prefrences": "{}", "recipes": [], "diet_restrictions": "{}", "username": "test1"}` |
|`GET`<br> `users/logout/`| None | Simple logout that does not do any real logging-out. | `"Successfully logged out"` |
|`GET`<br> `users/` | None | Returns list of all users as dictionaries | `[{"intolerances": "{}", "email": "test1@gmail.com", "id": 4, "ingredient_prefrences": "{}", "recipes": [], "diet_restrictions": "{}", "username": "test1"}, {...}]`|
|`GET`<br> `users/<pk>/` | None | Returns list of user with `pk` as a dictionary | `{"intolerances": "{}", "email": "test1@gmail.com", "id": 4, "ingredient_prefrences": "{}", "recipes": [], "diet_restrictions": "{}", "username": "test1"}`|
|`PATCH`<br> `users/<pk>/intolerances/add` | `{"intolerances": ["dairy"]}` | Adds `dairy` to the intolerances for user `<pk>`| `{"intolerances": "{\"diary\": 1}", "email": "test2@gmail.com", "id": <pk>, "ingredient_prefrences": "{}", "recipes": [{...}], "diet_restrictions": "{}","username": "test2"}`|
|`PATCH<br>` `users/<pk>/intolerances/remove` | `{"intolerances": ["dairy"]}` | Removes `dairy` from the intolerances for user `<pk>`| `{"intolerances": "{}", "email": "test2@gmail.com", "id": <pk>, "ingredient_prefrences": "{}", "recipes": [{...}], "diet_restrictions": "{}","username": "test2"}`|
|`PATCH`<br> `users/<pk>/ingredient_prefrences/add` | `{"ingredient_prefrences": ["healthy"]}` | Adds `healthy` to the ingredient_prefrences for user `<pk>`| `{"intolerances": "{}", "email": "test2@gmail.com", "id": <pk>, "ingredient_prefrences": "{\"healthy\": 1}", "recipes": [{...}], "diet_restrictions": "{}","username": "test2"}`|
|`PATCH`<br> `users/<pk>/ingredient_prefrences/remove` | `{"ingredient_prefrences": ["healthy"]}` | Removes `healthy` from the ingredient_prefrences for user `<pk>`| `{"intolerances": "{}", "email": "test2@gmail.com", "id": <pk>, "ingredient_prefrences": "{}", "recipes": [{...}], "diet_restrictions": "{}","username": "test2"}`|
|`PATCH`<br> `users/<pk>/diet_restrictions/add` | `{"diet_restrictions": ["vegan"]}` | Adds `vegan` to the diet_restrictions for user `<pk>`| `{"intolerances": "{}", "email": "test2@gmail.com", "id": <pk>, "ingredient_prefrences": "{}", "recipes": [{...}],"diet_restrictions": "{\"vegan\": 1}","username": "test2"}`|
|`PATCH`<br> `users/<pk>/diet_restrictions/remove` | `{"diet_restrictions": ["vegan"]}` | Removes `vegan` from the diet_restrictions for user `<pk>`| `{"intolerances": "{}", "email": "test2@gmail.com", "id": <pk>, "ingredient_prefrences": "{}", "recipes": [{...}], "diet_restrictions": "{}","username": "test2"}`|
|`DELETE`<br> `users/<pk>/` | None | Deletes the user with <pk> id. | `"User <pk> successfully deleted"`|
|`POST`<br> `users/<pk>/pantry/` | `{"food_list": ["tomatoes", "limes"]}` | Creates a new pantry associated with the user with with an id = pk.  Returns a dictionary of the pantry. Note, it will not create a pantry if a user already has one.| `{"food_dict": {"tomatoes": 1, "limes": 1}, "id": 2, "user_id": 3}`|
|`GET`<br> `users/<pk>/pantry/` | None | Gets the pantry associated with the user with with an id = pk.  Returns a dictionary of the pantry | `{"food_dict": {"carrots": 1, "tomatoes": 1}, "id": 2, "user_id": 3}`|
|`PATCH`<br> `pantry/<pk>/add/` | `{"food_list": ["apples"]}` | Adds a comma seperated list to the food_list attribute of the pantry.  Returns the updated pantry object |  `{"food_dict": {"tomatoes": 1, "limes": 1, "apples": 1}, "id": 2, "user_id": 3}` 
|`PATCH`<br> `pantry/<pk>/remove/` | `{"food_list": ["apples"]}` | Removes a comma seperated list to the food_list attribute of the pantry.  Returns the updated pantry object |  `{"food_dict": {"tomatoes": 1, "limes": 1}, "id": 2, "user_id": 3}` |
|`DELETE`<br> `pantry/<pk>` | None | Removes pantry from user object | `"Pantry <pk> successfully deleted"`|
|`POST`<br> `users/<pk>/recipes/` | `{"name": "Numba 2", "ingredients": ["limes", "carrots"], "instructions": "1. do this first, 2. do this second", "nutritional_data": 37, "url": "Bla.com", "user_state": 1}` | Creates new recipe associated with user with id = pk.  Returns a dict of the new recipe | `{"id": 4, "user": 4, "name": "Numba 2", "ingredients": "{\"limes\": 1, \"carrots\": 1}", "instructions": "1. do this first, 2. do this second", "nutritional_data": 37, "url": "Bla.com", "user_state": 1}`|
|`GET`<br> `users/<pk>/recipes/` | Optional Params: `pantry=True` or `ingredients=apples, limes` | Gets recipes associated with a user.  If param pantry is active, it gets recipes with ingredients that are in pantry and if ingredients param is active, it gets recipes with corresponding ingredients.  Returns a list of recipes. | `[{"id": 3,  "user": 4, "name": "Numba 2", "ingredients": "{\"limes\": 1, \"carrots\": 1}", "instructions": "1. do this first, 2. do this second", "nutritional_data": 37, "url": "Bla.com", "user_state": 1}, {...}]`|
|`PATCH`<br> `recipes/<pk>/neutralize/` | None | Updates the user_state attribute of recipe with pk to neutralize the user_state attribute with a value of 0.  Returns dictionary of the updated recipe.  | `{"id": 1, "user": 4, "name": "test4", "ingredients": {"apples": 1, "carrots": 1}, "instructions": "1. do this first, 2. do this second", "nutritional_data": 37, "url": "Bla.com", "user_state": 0}`|
|`PATCH`<br> `recipes/<pk>/favorite/` | None | Updates the user_state attribute of recipe with pk to favorite the user_state attribute with a value of 1.  Returns dictionary of the updated recipe.  | `{"id": 1, "user": 4, "name": "test4", "ingredients": {"apples": 1, "carrots": 1}, "instructions": "1. do this first, 2. do this second", "nutritional_data": 37, "url": "Bla.com", "user_state": 1}`|
|`PATCH`<br> `recipes/<pk>/unfavorite/` | None | Updates the user_state attribute of recipe with pk to unfavorite the user_state attribute with a value of 0.  Returns dictionary of the updated recipe.  | `{"id": 1, "user": 4, "name": "test4", "ingredients": {"apples": 1, "carrots": 1}, "instructions": "1. do this first, 2. do this second", "nutritional_data": 37, "url": "Bla.com", "user_state": -1}`|
|`DELETE`<br> `recipes/<pk>` | None | Deletes recipe with <pk>  | `Recipe <pk> successfully deleted`|





