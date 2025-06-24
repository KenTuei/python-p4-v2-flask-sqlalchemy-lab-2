from models import db, Customer, Item, Review
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    c1 = Customer(name="Tal Yuri")
    c2 = Customer(name="Aria Stone")

    i1 = Item(name="Laptop Backpack", price=49.99)
    i2 = Item(name="Insulated Coffee Mug", price=9.99)
    i3 = Item(name="Notebook", price=3.49)

    r1 = Review(comment="Great quality!", customer=c1, item=i1)
    r2 = Review(comment="Perfect for travel", customer=c1, item=i2)
    r3 = Review(comment="Affordable and useful", customer=c2, item=i3)

    db.session.add_all([c1, c2, i1, i2, i3, r1, r2, r3])
    db.session.commit()