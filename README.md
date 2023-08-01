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
<!-- 1. Create a `.env` file with your API keys
    ```bash
    # .env

    # LocationIQ API key
    LOCATION_KEY="replace_with_your_api_key"

    # OpenWeather API Key
    WEATHER_KEY="replace_with_your_api_key"
    ``` -->

1. Run the django server from directory with `manage.py` file
    - `python manage.py runserver`

## Endpoints

| Route | Query Parameter(s) | Route Description | Response |
|--|--|--|--|
|`GET` `rest_api/login/`| None | Dummy Route for login| `"Successfully logged in"` |
|`GET` `rest_api/logout/`| None | Dummy Route for logout| `"Successfully logged out"` |
|`GET` `rest_api/users/` | None | Returns list of all users as dictionaries | `[{"id": 2, "last_login": "2023-07-28T19:25:07.547485Z", "is_superuser": true, "username": "user1", "first_name": "User", "last_name": "Profile", "email": "ada@email.com", "is_staff": false, "is_active": true,"date_joined": "2023-07-28T19:24:32.195340Z", "alergies": {}, "restrictions": {}, "prefrences": {}}, {...}]`|
|`GET` `rest_api/users/<pk>/` | None | Returns list of user with `pk` as a dictionary | `[{"id": <pk>, "last_login": "2023-07-28T19:25:07.547485Z", "is_superuser": true, "username": "user1", "first_name": "User", "last_name": "Profile", "email": "ada@email.com", "is_staff": false, "is_active": true,"date_joined": "2023-07-28T19:24:32.195340Z", "alergies": {}, "restrictions": {}, "prefrences": {}}]`|
|`POST` `rest_api/users/` | `{"username": "test6", "password": "user0987", "email": "test_email@email.com", "alergies": "eggs, nuts", "first_name": "Bla", "last_name": "Dee", "prefrences": "", "restrictions": ""}` | Creates new User object. And returns a dictionary of the new User object. | `{"id": <pk>, "last_login": "2023-07-28T19:25:07.547485Z", "is_superuser": true, "username": "user1", "first_name": "User", "last_name": "Profile", "email": "ada@email.com", "is_staff": false, "is_active": true,"date_joined": "2023-07-28T19:24:32.195340Z", "alergies": {}, "restrictions": {}, "prefrences": {}}`|
|`DELETE` `rest_api/users/<pk>/` | None | Deletes the user with <pk> id. | `"Successfully deleted <first_name> <last_name>: <username>"`|
|`GET` `rest_api/users/<pk>/pantry/` | None | Gets the pantry associated with the user with with an id = pk.  Returns a dictionary of the pantry | `{"id": 8, "user": 4, "food_list": { "limes": 1, "tomatoes": 1}, "updated": "2023-07-31T00:00:00Z"}`|
|`GET` `rest_api/users/<pk>/pantry/` | None | Gets the pantry associated with the user with with an id = pk.  Returns a dictionary of the pantry | `{"id": 8, "user": 4, "food_list": { "limes": 1, "tomatoes": 1}, "updated": "2023-07-31T00:00:00Z"}`|
|`POST` `rest_api/users/<pk>/pantry/` | `{"food_list": ["tomatoes", "limes"]}` | Creates a newpantr y associated with the user with with an id = pk.  Returns a dictionary of the pantry. | `{"id": 8, "user": 4, "food_list": { "limes": 1, "tomatoes": 1}, "updated": "2023-07-31T00:00:00Z"}`|
|`PATCH` `rest_api/users/<pk>/pantry/add/` | `{"food_list": ["apples"]}` | Adds a comma seperated list to the food_list attribute of the pantry.  Returns the updated pantry object | `{"id": 8, "user": 4, "food_list": { "limes": 1, "tomatoes": 1, "apples": 1}, "updated": "2023-07-31T00:00:00Z"}`|
|`PATCH` `rest_api/users/<pk>/pantry/remove/` | `{"food_list": ["apples"]}` | Removes a comma seperated list from the food_list attribute of the pantry.  Returns the updated pantry object | `{"id": 8, "user": 4, "food_list": { "limes": 1, "tomatoes": 1}, "updated": "2023-07-31T00:00:00Z"}`|
|`DELETE` `rest_api/users/<pk>/pantry/` | None | Removes pantry from user object | `Pantry successflly deleted: id = <pk>`|
|`POST` `rest_api/users/<pk>/recipes/` | `{"name": "Numba 2", "ingredients": ["limes", "carrots"], "instructions": "1. do this first, 2. do this second", "nutritional_data": 37.307826086956524, "url": "Bla.com", "user_state": 1}` | Creates new recipe associated with user with id = pk.  Returns a dict of the new recipe | `{"id": 4, "user": 4, "name": "Numba 2", "ingredients": {"limes": 1, "carrots": 1}, "instructions": "1. do this first, 2. do this second", "nutritional_data": 37.307826086956524, "url": "Bla.com", "user_state": 1}`|
|`GET` `rest_api/users/<pk>/recipes/` | Optional Params: `pantry=True` or `ingredients=apples, limes` | Gets recipes associated with a user.  If param pantry is active, it gets recipes with ingredients that are in pantry and if ingredients param is active, it gets recipes with corresponding ingredients.  Returns a list of recipes. | `[{"id": 3,  "user": 4, "name": "Numba 2", "ingredients": {"limes": 1, "carrots": 1}, "instructions": "1. do this first, 2. do this second", "nutritional_data": 37.307826086956524, "url": "Bla.com", "user_state": 1}, {...}]`|
|`PATCH` `rest_api/recipes/<pk>/neutralize/` | None | Updates the user_state attribute of recipe with pk to neutralize the user_state attribute with a value of 0.  Returns dictionary of the updated recipe.  | `{"id": 1, "user": 4, "name": "test4", "ingredients": {"apples": 1, "carrots": 1}, "instructions": "1. do this first, 2. do this second", "nutritional_data": 37.307826086956524, "url": "Bla.com", "user_state": 0}`|
|`PATCH` `rest_api/recipes/<pk>/favorite/` | None | Updates the user_state attribute of recipe with pk to favorite the user_state attribute with a value of 1.  Returns dictionary of the updated recipe.  | `{"id": 1, "user": 4, "name": "test4", "ingredients": {"apples": 1, "carrots": 1}, "instructions": "1. do this first, 2. do this second", "nutritional_data": 37.307826086956524, "url": "Bla.com", "user_state": 1}`|
|`PATCH` `rest_api/recipes/<pk>/unfavorite/` | None | Updates the user_state attribute of recipe with pk to unfavorite the user_state attribute with a value of 0.  Returns dictionary of the updated recipe.  | `{"id": 1, "user": 4, "name": "test4", "ingredients": {"apples": 1, "carrots": 1}, "instructions": "1. do this first, 2. do this second", "nutritional_data": 37.307826086956524, "url": "Bla.com", "user_state": -1}`|





