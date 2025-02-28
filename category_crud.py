from app import app, db
from models import Category, Restaurant

def create_category(name, restaurant_id):
    with app.app_context():
        categeroies = Category.query.filter_by(restaurant_id=restaurant_id).all()
        for category in categeroies:
            if category.name == name:
                print('A category named like this already exists for this restaurant')
                return None
            
        category = Category(name=name, restaurant_id=restaurant_id)
        db.session.add(category)
        db.session.commit()
        return category
    
def update_category(category_id, attrs: dict):
    with app.app_context():
        category = Category.query.get(category_id)
        if category:
            for key, value in attrs.items():
                setattr(category, key, value)
            db.session.commit()
            return category
        return None
    
def delete_category(category_id):
    with app.app_context():
        category = Category.query.get(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()
            return True
        return False