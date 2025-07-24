from typing import List
from app.core.ports.related_products_port import RelatedProductsPort
from app.core.domain.product_model import RelatedProduct

class GetRelatedProductsUseCase:
    def __init__(self, related_products_port: RelatedProductsPort):
        self.related_products_port = related_products_port

    def execute(self, product_id: str) -> List[RelatedProduct]:
        return self.related_products_port.get_related_products(product_id)