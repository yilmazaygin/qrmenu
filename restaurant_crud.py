from app import db, app
from models import Restaurant


def create_restaurant(name):
    with app.app_context():
        restaurants = Restaurant.query.filter_by(name=name).all()
        for restaurant in restaurants:
            if restaurant.name == name:
                print('A restaurant named like this already exists')
                return None

        restaurant = Restaurant(name=name)
        db.session.add(restaurant)
        db.session.commit()
        return restaurant
    
def update_restaurant(restaurant_id, attrs: dict):
    with app.app_context():
        restaurant = Restaurant.query.get(restaurant_id)
        if restaurant:
            for key, value in attrs.items():
                setattr(restaurant, key, value)
            db.session.commit()
            return restaurant
        return None
    
def delete_restaurant(restaurant_id):
    with app.app_context():
        restaurant = Restaurant.query.get(restaurant_id)
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            return True
        return False    