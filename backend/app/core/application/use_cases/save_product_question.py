from typing import List
from app.core.domain.product_model import Question
from app.core.ports.product_repository import ProductRepository

class SaveProductQuestionsUseCase:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def execute(self, product_id: str, question_text: str) -> Question:
        return self.product_repository.save_question(product_id, question_text)