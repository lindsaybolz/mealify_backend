import pytest
from app import create_app
from app import db
from app.models.pantry import Pantry
from app.models.user import User
from app.models.recipe import Recipe
# from flask.signals import request_finished



@pytest.fixture
def app():
    # create the app with a test config dictionary
    app = create_app(test_config=True)

    # @request_finished.connect_via(app)
    # def expire_session(sender, response, **extra):
    #       db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    # close and remove the temporary database
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_users(client):
    user_1 = User(username="tester1", password="testing123", email='test1@gmail.com')
    user_2 = User(username="tester2", password="testing123", email='test2@gmail.com')

    db.session.add_all([user_1, user_2])
    db.session.commit()

@pytest.fixture
def one_saved_user_with_two_recipes_and_pantry(client):
    recipe_1 = Recipe(
        title="Recipe1", 
        ingredients={'item1': 1, 'item2': 1},
        instructions='Instructions1',
        url='url1',
        nutritional_data=1,
        user_state=1,
    )
    recipe_2 = Recipe(
        title="Recipe2", 
        ingredients={'item3': 1, 'item4': 1},
        instructions='Instructions2',
        url='url2',
        nutritional_data=2,
        user_state=1,
    )
    pantry_1 = Pantry(
        food_dict={'food1': 1, 'food2': 1}
    )

    user_1 = User(
        username="tester1", 
        password="testing123", 
        email='test1@gmail.com', 
        recipes=[recipe_1, recipe_2], 
        pantry=pantry_1)

    db.session.add_all([user_1])
    db.session.commit()
