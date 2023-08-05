class Pantry(models.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food_list = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates='recipe', uselist=False)

    def to_dict(self):
        return {
            'id': self.pk,
            'user': self.user.pk,
            'food_list': self.food_list,
        }
