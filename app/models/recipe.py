import sqlalchemy as sa
from app import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text)
    instructions = db.Column(db.Text)
    nutritional_data = db.Column(db.Float)
    url = db.Colummn(db.Float)
    user_state = db.Column(db.Integer, sa.CheckConstraint('age > 0 AND age < 100'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates='recipe')

    def to_dict(self):
        return {
            'id': self.pk,
            'user': self.user.pk,
            'title': self.title,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
            'nutritional_data': self.nutritional_data,
            'url': self.url,
            'user_state': self.user_state,
        }