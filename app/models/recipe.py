import sqlalchemy as sa
from app import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.JSON, default=lambda: {})
    instructions = db.Column(db.String, default='')
    nutritional_data = db.Column(db.Integer, default=0)
    url = db.Column(db.String(50), default='')
    user_state = db.Column(db.Integer, sa.CheckConstraint('user_state > -2 AND user_state < 2'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates='recipes')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'ingredients': self.ingredients,
            'instructions': self.instructions,
            'nutritional_data': self.nutritional_data,
            'url': self.url,
            'user_state': self.user_state,
        }
    
    @classmethod
    def from_dict(cls, dict_data):

        new_recipe = Recipe(
            user = dict_data['user'],
            user_id = dict_data['user_id'], 
            title = dict_data['title'],
            ingredients = dict_data['ingredients'],
            instructions = dict_data['instructions'],
            nutritional_data = dict_data['nutritional_data'],
            url = dict_data['url'],
            user_state = dict_data['user_state'],
        )

        return new_recipe
