from app import db
    
class Pantry(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food_dict = db.Column(db.JSON, default=lambda: {})
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates='pantry' )

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'food_dict': self.food_dict,
        }
    
    @classmethod
    def from_dict(cls, dict_data):

        new_recipe = Pantry(
            user = dict_data['user'],
            user_id = dict_data['user_id'], 
            food_dict = dict_data['food_dict']
        )

        return new_recipe

