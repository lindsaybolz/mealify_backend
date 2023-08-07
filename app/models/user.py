from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    alergies = db.Column(db.String, unique=True)
    prefrences = db.Column(db.String, unique=True)
    restrictions = db.Column(db.String, unique=True)
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
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'alergies': self.alergies,
            'restrictions': self.restrictions,
            'prefrences': self.prefrences,
            'recipes': recipes,
            # 'pantry': self.pantry,
        }
