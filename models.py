from flask_sqlalchemy import SQLAlchemy

# Flask SQLAlchemy instance
db = SQLAlchemy()

class Restaurant(db.Model):
    """
    Represents a restaurant in the system. Each restaurant can have multiple categories of products.
    """
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each restaurant
    name = db.Column(db.String(100), nullable=False)  # Name of the restaurant
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Timestamp when the restaurant was created
    paid_until = db.Column(db.DateTime, nullable=True)  # Payment expiration date, if applicable
    payment_amount = db.Column(db.Float, nullable=True)  # Payment amount associated with the restaurant (if any)

    # Relationship: Each restaurant can have multiple categories
    categories = db.relationship('Category', back_populates='restaurant', cascade="all, delete-orphan")


class Category(db.Model):
    """
    Represents a product category in a restaurant.
    Each category can have multiple products under it.
    """
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each category
    name = db.Column(db.String(100), nullable=False)  # Name of the category (e.g., Beverages, Main Courses)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)  # Foreign key linking to the restaurant

    # Relationship: Each category is linked to a restaurant
    restaurant = db.relationship('Restaurant', back_populates='categories')

    # Relationship: Each category can have multiple products
    products = db.relationship('Product', backref='category', cascade="all, delete-orphan")


class Product(db.Model):
    """
    Represents a product offered by a restaurant under a specific category.
    A product can have an optional promotion and stores its last price for reference.
    """
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each product
    name = db.Column(db.String(100), nullable=False)  # Name of the product (e.g., Burger, Pizza)
    description = db.Column(db.Text, nullable=True)  # Description of the product (optional)
    price = db.Column(db.Float, nullable=False)  # Current price of the product
    image_url = db.Column(db.String(255), nullable=True)  # URL of the product image (optional)
    position = db.Column(db.Integer, nullable=False, default=0)  # Position for sorting products within the category
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)  # Foreign key linking to the category

    # Flag indicating whether the product has a promotion applied
    promotion = db.Column(db.Boolean, default=False)  # If the product has a promotion or not

    # Stores the last price of the product before any price changes
    last_price = db.Column(db.Float, nullable=True) # Last price of the product

    # Alergens are entered as a short text
    allergens = db.Column(db.String(255), nullable=True)  # List of allergens in the product
