from app.core.domain.product_model import Product
from app.core.ports.product_repository import ProductRepository

class SaveProductUseCase:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def execute(self, product: Product) -> Product: 
        return self.product_repository.save_product(product)