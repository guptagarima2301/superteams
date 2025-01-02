from faker import Faker
from database import SessionLocal
from models import Customer, Product, Transaction
import random

faker = Faker()
db = SessionLocal()

# Add Customers
for _ in range(50):
    customer = Customer(
        name=faker.name(),
        age=random.randint(18, 70),
        gender=random.choice(["Male", "Female", "Other"]),
        city=faker.city(),
        country=faker.country(),
        email=faker.email(),
        phone=faker.phone_number(),
    )
    db.add(customer)

# Add Products
for _ in range(50):
    product = Product(
        name=faker.word(),
        category=random.choice(["T-Shirt", "Trousers", "Shoes", "Accessories"]),
        short_description=faker.sentence(),
        description=faker.text(),
        brand=random.choice(["Zara", "Mango", "Zudio"]),
        color=random.choice(["Red", "Blue", "Black", "White"]),
        price=round(random.uniform(10, 100), 2),
        currency="USD",
        tags=", ".join(faker.words(nb=3)),
    )
    db.add(product)

db.commit()
