from abc import ABC, abstractmethod
from typing import Optional, List
from app.core.domain.product_model import Product, Question

class ProductRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Product]:
        pass

    @abstractmethod
    def get_by_id(self, product_id: str) -> Optional[Product]:
        pass

    @abstractmethod
    def save_product(self, product: Product) -> Product:
        pass

    @abstractmethod
    def remove_product(self, product_id: str) -> None:
        pass

    @abstractmethod
    def save_question(self, product_id: str, question_text: str) -> Question:
        pass