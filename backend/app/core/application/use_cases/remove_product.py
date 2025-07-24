from typing import Optional
from app.core.ports.product_repository import ProductRepository

class RemoveProductUseCase:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def execute(self, product_id: str) -> None:
        return self.product_repository.remove_product(product_id)