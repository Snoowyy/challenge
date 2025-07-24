from abc import ABC, abstractmethod
from typing import List
from app.core.domain.product_model import RelatedProduct

class RelatedProductsPort(ABC):

    @abstractmethod
    def get_related_products(self, product_id: str) -> List[RelatedProduct]:
        pass