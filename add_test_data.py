# CREATING DATABASE, ADDING 3 RESTAURANTS, 10 CATEGORIES, AND 34 PRODUCTS

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db, Restaurant, Category, Product  # Importing models from models.py

# Set up the application and database configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qrmenu_db.db'  # Database name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Function to create the database and insert sample data
def create_db_and_insert_data():
    # Create the database and tables
    with app.app_context():
        db.create_all()  # Create the database and tables

    # Create 3 restaurants
    restaurant1 = Restaurant(
        name='Pizza Express',
        paid_until=datetime(2025, 12, 31),
        payment_amount=500.00
    )
    restaurant2 = Restaurant(
        name='Sushi World',
        paid_until=datetime(2025, 6, 30),
        payment_amount=300.00
    )
    restaurant3 = Restaurant(
        name='Burger King',
        paid_until=datetime(2025, 9, 15),
        payment_amount=400.00
    )

    db.session.add_all([restaurant1, restaurant2, restaurant3])
    db.session.commit()

    # Create 10 categories
    categories = [
        Category(name='Pizzas', restaurant_id=restaurant1.id),
        Category(name='Beverages', restaurant_id=restaurant1.id),
        Category(name='Pasta', restaurant_id=restaurant1.id),
        Category(name='Sushi', restaurant_id=restaurant2.id),
        Category(name='Sashimi', restaurant_id=restaurant2.id),
        Category(name='Drinks', restaurant_id=restaurant2.id),
        Category(name='Burgers', restaurant_id=restaurant3.id),
        Category(name='Fries', restaurant_id=restaurant3.id),
        Category(name='Salads', restaurant_id=restaurant3.id),
        Category(name='Desserts', restaurant_id=restaurant3.id)
    ]

    db.session.add_all(categories)
    db.session.commit()

    # Create 34 products
    products = [
        # Pizza Express (restaurant1)
        Product(name='Margherita Pizza', description='Classic Margherita with fresh mozzarella and basil', price=9.99, category_id=categories[0].id, promotion=False, last_price=9.99, allergens='Gluten, Dairy'),
        Product(name='Pepperoni Pizza', description='Pepperoni and cheese topped pizza', price=12.99, category_id=categories[0].id, promotion=True, last_price=13.99, allergens='Gluten, Dairy'),
        Product(name='Hawaiian Pizza', description='Pizza with ham, pineapple, and cheese', price=13.49, category_id=categories[0].id, promotion=False, last_price=13.49, allergens='Gluten, Dairy'),
        Product(name='Veggie Pizza', description='A mix of fresh vegetables on a pizza base', price=11.49, category_id=categories[0].id, promotion=False, last_price=11.49, allergens='Gluten, Dairy'),
        Product(name='Carbonara Pasta', description='Pasta with creamy carbonara sauce and pancetta', price=11.49, category_id=categories[2].id, promotion=False, last_price=11.49, allergens='Gluten, Dairy'),
        Product(name='Coca Cola', description='Refreshing Coca Cola', price=1.99, category_id=categories[1].id, promotion=True, last_price=1.99, allergens='None'),
        Product(name='Sprite', description='Lemon-lime soda', price=1.89, category_id=categories[1].id, promotion=False, last_price=1.99, allergens='None'),
        Product(name='Iced Tea', description='Cool and refreshing iced tea', price=2.49, category_id=categories[1].id, promotion=True, last_price=2.49, allergens='None'),
        
        # Sushi World (restaurant2)
        Product(name='California Roll', description='Rice, avocado, crab, and cucumber wrapped in seaweed', price=14.99, category_id=categories[3].id, promotion=False, last_price=14.99, allergens='Fish, Gluten'),
        Product(name='Salmon Sashimi', description='Fresh sliced salmon', price=16.49, category_id=categories[4].id, promotion=False, last_price=16.49, allergens='Fish'),
        Product(name='Tuna Nigiri', description='Tuna on a bed of rice with a dash of wasabi', price=9.99, category_id=categories[3].id, promotion=True, last_price=10.99, allergens='Fish'),
        Product(name='Miso Soup', description='Warm miso soup with tofu and seaweed', price=3.99, category_id=categories[5].id, promotion=False, last_price=3.99, allergens='Soy'),
        Product(name='Japanese Green Tea', description='Hot green tea', price=2.49, category_id=categories[5].id, promotion=False, last_price=2.49, allergens='None'),
        Product(name='Dragon Roll', description='A roll with shrimp tempura and avocado', price=18.99, category_id=categories[3].id, promotion=False, last_price=18.99, allergens='Fish, Gluten'),
        Product(name='Eel Nigiri', description='Fresh eel on sushi rice', price=11.49, category_id=categories[4].id, promotion=False, last_price=11.49, allergens='Fish'),
        
        # Burger King (restaurant3)
        Product(name='Cheeseburger', description='Classic cheeseburger with lettuce, tomato, and cheese', price=7.49, category_id=categories[6].id, promotion=False, last_price=7.49, allergens='Gluten, Dairy'),
        Product(name='Chicken Nuggets', description='Crispy chicken nuggets with dipping sauce', price=5.99, category_id=categories[7].id, promotion=True, last_price=6.49, allergens='Gluten, Dairy'),
        Product(name='French Fries', description='Crispy golden fries', price=2.99, category_id=categories[7].id, promotion=True, last_price=3.49, allergens='None'),
        Product(name='Caesar Salad', description='Crisp lettuce with Caesar dressing and croutons', price=6.99, category_id=categories[8].id, promotion=False, last_price=6.99, allergens='Dairy, Gluten'),
        Product(name='Chocolate Sundae', description='Creamy vanilla ice cream topped with chocolate sauce', price=3.49, category_id=categories[9].id, promotion=False, last_price=3.49, allergens='Dairy'),
        Product(name='Whopper', description='Signature flame-grilled burger with all the fixings', price=8.99, category_id=categories[6].id, promotion=True, last_price=9.49, allergens='Gluten, Dairy'),
        Product(name='Veggie Burger', description='Grilled veggie patty with lettuce, tomato, and sauce', price=7.49, category_id=categories[6].id, promotion=False, last_price=7.49, allergens='Gluten, Dairy'),
        Product(name='Onion Rings', description='Crispy golden onion rings', price=3.49, category_id=categories[7].id, promotion=False, last_price=3.49, allergens='None'),
        Product(name='Apple Pie', description='Classic apple pie dessert', price=2.99, category_id=categories[9].id, promotion=False, last_price=2.99, allergens='Gluten, Dairy'),
        Product(name='Milkshake', description='Creamy vanilla milkshake', price=4.99, category_id=categories[9].id, promotion=False, last_price=4.99, allergens='Dairy'),
        Product(name='Chicken Fries', description='Crispy chicken fries served with dipping sauces', price=4.49, category_id=categories[7].id, promotion=True, last_price=4.99, allergens='Gluten, Dairy'),
        Product(name='Double Cheeseburger', description='Two beef patties with melted cheese and condiments', price=9.49, category_id=categories[6].id, promotion=False, last_price=9.49, allergens='Gluten, Dairy'),
        Product(name='Fish Sandwich', description='Crispy fish fillet with tartar sauce', price=6.99, category_id=categories[6].id, promotion=False, last_price=6.99, allergens='Gluten, Fish'),
        Product(name='BBQ Bacon Burger', description='Burger with BBQ sauce and crispy bacon', price=10.49, category_id=categories[6].id, promotion=False, last_price=10.49, allergens='Gluten, Dairy'),
        
        # Additional Products
        Product(name='Four Cheese Pizza', description='A mix of mozzarella, cheddar, gouda, and parmesan', price=13.99, category_id=categories[0].id, promotion=False, last_price=13.99, allergens='Gluten, Dairy'),
        Product(name='BBQ Chicken Pizza', description='BBQ sauce topped with grilled chicken and veggies', price=14.49, category_id=categories[0].id, promotion=False, last_price=14.49, allergens='Gluten, Dairy'),
        Product(name='Tempura Roll', description='Shrimp tempura rolled with avocado and cucumber', price=16.99, category_id=categories[3].id, promotion=True, last_price=17.49, allergens='Fish, Gluten'),
        Product(name='Rainbow Roll', description='Variety of fresh fish on a California roll base', price=17.49, category_id=categories[3].id, promotion=False, last_price=17.49, allergens='Fish, Gluten'),
        Product(name='Shrimp Tempura', description='Lightly battered shrimp served with dipping sauce', price=12.99, category_id=categories[3].id, promotion=False, last_price=12.99, allergens='Fish, Gluten'),
    ]

    db.session.add_all(products)
    db.session.commit()

    print("Database created, 3 restaurants, 10 categories, and 34 products added.")

# Run the application and create the database when starting
if __name__ == "__main__":
    with app.app_context():
        create_db_and_insert_data()
