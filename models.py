from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    city = Column(String)
    country = Column(String)
    email = Column(String)
    phone = Column(String)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(String)
    short_description = Column(String)
    description = Column(String)
    brand = Column(String)
    color = Column(String)
    price = Column(Float)
    currency = Column(String)
    tags = Column(String)

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    amount_paid = Column(Float)
    purchase_date = Column(DateTime)
    if_returned = Column(Boolean)
    rating = Column(Float)
    review_text = Column(String)
