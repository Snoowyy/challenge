import json
from typing import Optional, List
from app.core.domain.product_model import Product, Question
from app.core.ports.product_repository import ProductRepository

class JSONProductRepository(ProductRepository):
    def __init__(self, db_path: str = "db.json"):
        with open(db_path, 'r', encoding='utf-8') as f:
            self._data = json.load(f)

    def get_all(self) -> List[Product]:
        return [Product(**product) for product in self._data['products']]

    def get_by_id(self, product_id: str) -> Optional[Product]:
        product_data = next((p for p in self._data['products'] if p['id'] == product_id), None)
        if product_data:
            return Product(**product_data)
        return None

    def save_product(self, product: Product) -> Product:
        product_data = next((p for p in self._data['products'] if p['id'] == product.id), None)

        if product_data:
            product_data.update(**product.model_dump())
            return Product(**product_data)
        self._data['products'].append(product.model_dump())

        with open("db.json", 'w', encoding='utf-8') as f:
            json.dump(self._data, f, indent=4)

        return product

    def remove_product(self, product_id: str) -> None:
        product_data = next((p for p in self._data['products'] if p['id'] == product_id), None)

        if product_data:
            self._data['products'].remove(product_data)
        else:
            raise Exception("Product not found")

        with open("db.json", 'w', encoding='utf-8') as f:
            json.dump(self._data, f, indent=4)

    def save_question(self, product_id: str, question_text: str) -> Question:
        product_data = next((p for p in self._data['products'] if p['id'] == product_id), None)

        if product_data:
            question = Question(id=(len(product_data['questions']) + 1), question=question_text)
            product_data['questions'].append(question)
            self._data['products'][self._data['products'].index(product_data)] = product_data
        else:
            raise Exception("Product not found")

        with open("db.json", 'w', encoding='utf-8') as f:
            json.dump(self._data, f, indent=4)

        return question
