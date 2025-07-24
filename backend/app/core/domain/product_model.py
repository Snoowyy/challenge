from pydantic import BaseModel, Field
from typing import List, Optional

class Price(BaseModel):
    currency: str
    real_amount: int
    discounted_amount: int
    discount: int

class Seller(BaseModel):
    name: str
    logo_url: str
    followers: int
    quantity_products: int
    is_mercado_lider: bool = False

class PaymentMethod(BaseModel):
    name: str
    logo_url: str

class Color(BaseModel):
    name: str
    thumbnail: str

class Variants(BaseModel):
    colors: List[Color]
    storage: List[int]
    ram: List[int]

class Rating(BaseModel):
    average: float
    reviews: int

class ProductInfo(BaseModel):
    title: str
    price: Price
    is_favorited: bool
    sold_quantity: int
    condition: str
    rating: Rating
    images: List[str]
    features: List[str]
    variants: Variants

class Range(BaseModel):
    min: float
    max: float
    current: float

class Characteristic(BaseModel):
    label: str
    value: str
    slider: bool = False
    range: Optional[Range] = None

class Question(BaseModel):
    id: int
    question: str
    answer: Optional[str] = None
    answer_date: Optional[str] = None

class RelatedProduct(BaseModel):
    name: str
    value: int

class Product(BaseModel):
    id: str
    product_info: ProductInfo
    description: str
    stock: int
    questions: List[Question]
    seller: Seller
    characteristics: List[Characteristic]
    payment_methods: Optional[List[PaymentMethod]] = None
    related_products: Optional[List[RelatedProduct]] = None

    class Config:
        populate_by_name = True
