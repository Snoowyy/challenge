from typing import List
from app.core.ports.product_repository import ProductRepository
from app.core.domain.product_model import Product

class GetAllProductsUseCase:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def execute(self) -> List[Product]:
        return self.product_repository.get_all()