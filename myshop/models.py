from myshop import db


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    availibility = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), nullable=False)

def __repr__(self):
    return self.title