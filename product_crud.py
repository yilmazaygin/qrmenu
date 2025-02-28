from app import db, app
from models import Product


def create_product(name, price, description, allergens, image_url, category_id, restaurant_id):
    with app.app_context():
        products = Product.query.filter_by(restaurant_id=restaurant_id).all()
        for product in products:
            if product.name == name:
                print('A product named like this already exists for this restaurant')
                return None

        product = Product(name=name, price=price, description=description, allergens=allergens, image_url=image_url, category_id=category_id, restaurant_id=restaurant_id)
        db.session.add(product)
        db.session.commit()
        return product

def update_product(product_id, attrs: dict):
    with app.app_context():
        product = Product.query.get(product_id)
        if product:
            for key, value in attrs.items():
                setattr(product, key, value)
            db.session.commit()
            return product
        return None

def delete_product(product_id):
    with app.app_context():
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return True
        return False

