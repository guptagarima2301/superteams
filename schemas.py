from pydantic import BaseModel
from typing import Optional

class CustomerBase(BaseModel):
    name: str
    age: int
    gender: str
    city: str
    country: str
    email: str
    phone: str

class ProductBase(BaseModel):
    name: str
    category: str
    short_description: str
    description: str
    brand: str
    color: str
    price: float
    currency: str
    tags: Optional[str]

class TransactionBase(BaseModel):
    product_id: int
    customer_id: int
    amount_paid: float
    purchase_date: str
    if_returned: Optional[bool] = False
    rating: Optional[float]
    review_text: Optional[str]

class ProductSearchResponse(BaseModel):
    name: str
    category: str
    price: float
    currency: str
    description: str
    recommendation_score: Optional[float] = None
