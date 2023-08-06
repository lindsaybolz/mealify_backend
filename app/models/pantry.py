from app import db
    
class Pantry(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food_list = db.Column(db.Text)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # user = db.relationship("User", backref='pantry', uselist=False)

    def to_dict(self):
        return {
            'id': self.id,
            # 'user': self.user.to_dict(),
            'food_list': self.food_list,
        }
