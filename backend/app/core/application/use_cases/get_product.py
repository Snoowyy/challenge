from typing import Optional
from app.core.domain.product_model import Product
from app.core.ports.product_repository import ProductRepository

class GetProductUseCase:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def execute(self, product_id: str) -> Optional[Product]:
        return self.product_repository.get_by_id(product_id)