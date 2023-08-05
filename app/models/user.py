from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.string(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    alergies = db.Column(db.String, unique=True, nullable=False)
    prefrences = db.Column(db.String, unique=True, nullable=False)
    restrictions = db.Column(db.String, unique=True, nullable=False)
    recipes = db.relationship("Recipe", back_populates='recipe',cascade = "all, delete-orphan")
    pantry = db.relationship("Pantry", back_populates='pantry',cascade = "all, delete-orphan" uselist=False)

    def __repr__(self):
        return self.username

    def to_dict(self):
        return {
            'pk': self.pk,
            'last_login': self.last_login,
            'is_superuser': self.is_superuser,
            'username': self.username,
            'email': self.email,
            'is_active': self.is_active,
            'alergies': self.alergies,
            'restrictions': self.restrictions,
            'prefrences': self.prefrences,
        }
