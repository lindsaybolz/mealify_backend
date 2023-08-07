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
|`POST` `users/register/`| `{"email": "example@example.com", "username": "example", "password": "example123"}` | Creates a new user| `{"alergies": "{}", "email": "example@example.com", "id": 1, "prefrences": "{}", "recipes": [], "restrictions": "{}", "username": "example"}` |
|`GET` `users/login/`| `{"email": "test@example.com", "password": "testing123"}` | Simple login that does not do any real authentication.| `{"alergies": "{}", "email": "test1@gmail.com", "id": 1, "prefrences": "{}", "recipes": [], "restrictions": "{}", "username": "test1"}` |
|`GET` `users/logout/`| None | Simple logout that does not do any real logging-out. | `"Successfully logged out"` |
|`GET` `users/` | None | Returns list of all users as dictionaries | `[{"alergies": "{}", "email": "test1@gmail.com", "id": 4, "prefrences": "{}", "recipes": [], "restrictions": "{}", "username": "test1"}, {...}]`|
|`GET` `users/<pk>/` | None | Returns list of user with `pk` as a dictionary | `{"alergies": "{}", "email": "test1@gmail.com", "id": 4, "prefrences": "{}", "recipes": [], "restrictions": "{}", "username": "test1"}`|
|`PATCH` `users/<pk>/alergies/add` | `{"alergies": ["dairy"]}` | Adds `dairy` to the alergies for user `<pk>`| `{"alergies": "{\"diary\": 1}", "email": "test2@gmail.com", "id": <pk>, "prefrences": "{}", "recipes": [{...}],"restrictions": "{}","username": "test2"}`|
|`PATCH` `users/<pk>/alergies/remove` | `{"alergies": ["dairy"]}` | Removes `dairy` from the alergies for user `<pk>`| `{"alergies": "{}", "email": "test2@gmail.com", "id": <pk>, "prefrences": "{}", "recipes": [{...}],"restrictions": "{}","username": "test2"}`|
|`PATCH` `users/<pk>/prefrences/add` | `{"prefrences": ["healthy"]}` | Adds `healthy` to the prefrences for user `<pk>`| `{"alergies": "{}", "email": "test2@gmail.com", "id": <pk>, "prefrences": "{\"healthy\": 1}", "recipes": [{...}],"restrictions": "{}","username": "test2"}`|
|`PATCH` `users/<pk>/prefrences/remove` | `{"prefrences": ["healthy"]}` | Removes `healthy` from the prefrences for user `<pk>`| `{"alergies": "{}", "email": "test2@gmail.com", "id": <pk>, "prefrences": "{}", "recipes": [{...}],"restrictions": "{}","username": "test2"}`|
|`PATCH` `users/<pk>/restrictions/add` | `{"restrictions": ["vegan"]}` | Adds `vegan` to the restrictions for user `<pk>`| `{"alergies": "{}", "email": "test2@gmail.com", "id": <pk>, "prefrences": "{}", "recipes": [{...}],"restrictions": "{\"vegan\": 1}","username": "test2"}`|
|`PATCH` `users/<pk>/restrictions/remove` | `{"restrictions": ["vegan"]}` | Removes `vegan` from the restrictions for user `<pk>`| `{"alergies": "{}", "email": "test2@gmail.com", "id": <pk>, "prefrences": "{}", "recipes": [{...}],"restrictions": "{}","username": "test2"}`|
|`DELETE` `users/<pk>/` | None | Deletes the user with <pk> id. | `"User <pk> successfully deleted"`|
|`POST` `users/<pk>/pantry/` | `{"food_list": ["tomatoes", "limes"]}` | Creates a new pantry associated with the user with with an id = pk.  Returns a dictionary of the pantry. Note, it will not create a pantry if a user already has one.| `{"food_dict": {"tomatoes": 1, "limes": 1}, "id": 2, "user_id": 3}`|
|`GET` `users/<pk>/pantry/` | None | Gets the pantry associated with the user with with an id = pk.  Returns a dictionary of the pantry | `{"food_dict": {"carrots": 1, "tomatoes": 1}, "id": 2, "user_id": 3}`|
|`PATCH` `pantry/<pk>/add/` | `{"food_list": ["apples"]}` | Adds a comma seperated list to the food_list attribute of the pantry.  Returns the updated pantry object |  `{"food_dict": {"tomatoes": 1, "limes": 1, "apples": 1}, "id": 2, "user_id": 3}` 
|`PATCH` `pantry/<pk>/remove/` | `{"food_list": ["apples"]}` | Removes a comma seperated list to the food_list attribute of the pantry.  Returns the updated pantry object |  `{"food_dict": {"tomatoes": 1, "limes": 1}, "id": 2, "user_id": 3}` |
|`DELETE` `pantry/<pk>` | None | Removes pantry from user object | `"Pantry <pk> successfully deleted"`|
|`POST` `users/<pk>/recipes/` | `{"name": "Numba 2", "ingredients": ["limes", "carrots"], "instructions": "1. do this first, 2. do this second", "nutritional_data": 37, "url": "Bla.com", "user_state": 1}` | Creates new recipe associated with user with id = pk.  Returns a dict of the new recipe | `{"id": 4, "user": 4, "name": "Numba 2", "ingredients": "{\"limes\": 1, \"carrots\": 1}", "instructions": "1. do this first, 2. do this second", "nutritional_data": 37, "url": "Bla.com", "user_state": 1}`|
|`GET` `users/<pk>/recipes/` | Optional Params: `pantry=True` or `ingredients=apples, limes` | Gets recipes associated with a user.  If param pantry is active, it gets recipes with ingredients that are in pantry and if ingredients param is active, it gets recipes with corresponding ingredients.  Returns a list of recipes. | `[{"id": 3,  "user": 4, "name": "Numba 2", "ingredients": "{\"limes\": 1, \"carrots\": 1}", "instructions": "1. do this first, 2. do this second", "nutritional_data": 37, "url": "Bla.com", "user_state": 1}, {...}]`|
|`PATCH` `recipes/<pk>/neutralize/` | None | Updates the user_state attribute of recipe with pk to neutralize the user_state attribute with a value of 0.  Returns dictionary of the updated recipe.  | `{"id": 1, "user": 4, "name": "test4", "ingredients": {"apples": 1, "carrots": 1}, "instructions": "1. do this first, 2. do this second", "nutritional_data": 37, "url": "Bla.com", "user_state": 0}`|
|`PATCH` `recipes/<pk>/favorite/` | None | Updates the user_state attribute of recipe with pk to favorite the user_state attribute with a value of 1.  Returns dictionary of the updated recipe.  | `{"id": 1, "user": 4, "name": "test4", "ingredients": {"apples": 1, "carrots": 1}, "instructions": "1. do this first, 2. do this second", "nutritional_data": 37, "url": "Bla.com", "user_state": 1}`|
|`PATCH` `recipes/<pk>/unfavorite/` | None | Updates the user_state attribute of recipe with pk to unfavorite the user_state attribute with a value of 0.  Returns dictionary of the updated recipe.  | `{"id": 1, "user": 4, "name": "test4", "ingredients": {"apples": 1, "carrots": 1}, "instructions": "1. do this first, 2. do this second", "nutritional_data": 37, "url": "Bla.com", "user_state": -1}`|
|`DELETE` `recipes/<pk>` | None | Deletes recipe with <pk>  | `Recipe <pk> successfully deleted`|





