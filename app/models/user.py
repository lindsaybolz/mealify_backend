from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    intolerances = db.Column(db.JSON, default=lambda: {})
    ingredient_preferences = db.Column(db.JSON, default=lambda: {})
    diet_restrictions = db.Column(db.JSON, default=lambda: {})
    recipes = db.relationship("Recipe", back_populates='user', cascade="all, delete-orphan")
    pantry = db.relationship("Pantry", back_populates='user', cascade="all, delete-orphan")

    # def __repr__(self):
    #     return self.username

    @classmethod
    def from_dict(cls, dict_data):
        return User(
            password=dict_data['password'], 
            email=dict_data['email'], 
            username=dict_data['username'])

    def to_dict(self):
        recipes = [recipe.to_dict() for recipe in self.recipes]
        try:
            pantry = self.pantry[0].to_dict()
        except:
            pantry = []
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'intolerances': self.intolerances,
            'diet_restrictions': self.diet_restrictions,
            'ingredient_preferences': self.ingredient_preferences,
            'recipes': recipes,
            'pantry': pantry,
        }
