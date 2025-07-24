from typing import List
from fastapi import APIRouter, HTTPException, Depends
from app.core.domain.product_model import Product, Question, RelatedProduct
from app.core.application.use_cases.get_all_products import GetAllProductsUseCase
from app.core.application.use_cases.get_product import GetProductUseCase
from app.core.application.use_cases.save_product import SaveProductUseCase
from app.core.application.use_cases.remove_product import RemoveProductUseCase
from app.core.application.use_cases.get_related_products import GetRelatedProductsUseCase
from app.core.application.use_cases.save_product_question import SaveProductQuestionsUseCase
from app.core.infrastructure.adapters.json_product_repository import JSONProductRepository
from app.core.infrastructure.adapters.ollama_adapter import OllamaRelatedProductsAdapter
from app.core.infrastructure.dto.questions_payload import QuestionPayload
router = APIRouter()

def get_all_products_use_case() -> GetAllProductsUseCase:
    repository = JSONProductRepository()
    return GetAllProductsUseCase(repository)

def get_product_use_case() -> GetProductUseCase:
    repository = JSONProductRepository()
    return GetProductUseCase(repository)

def save_product_use_case() -> SaveProductUseCase:
    repository = JSONProductRepository()
    return SaveProductUseCase(repository)

def remove_product_use_case() -> RemoveProductUseCase:
    repository = JSONProductRepository()
    return RemoveProductUseCase(repository)

def save_questions_use_case() -> SaveProductQuestionsUseCase:
    repository = JSONProductRepository()
    return SaveProductQuestionsUseCase(repository)

def get_related_products_use_case() -> GetRelatedProductsUseCase:
    adapter = OllamaRelatedProductsAdapter()
    return GetRelatedProductsUseCase(adapter)

@router.get("/api/products", response_model=List[Product])
def get_all_products(
    use_case: GetAllProductsUseCase = Depends(get_all_products_use_case)
):
    try:
        products = use_case.execute()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/products/{product_id}", response_model=Product)
def get_product(
    product_id: str,
    use_case: GetProductUseCase = Depends(get_product_use_case)
):
    try:
        product = use_case.execute(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/products", response_model=Product)
def save_product(
    payload: Product,
    use_case: SaveProductUseCase = Depends(save_product_use_case)
):
    try:
        product = use_case.execute(payload)
        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/api/products/{product_id}", response_model=None)
def remove_product(
    product_id: str,
    use_case: RemoveProductUseCase = Depends(remove_product_use_case)
):
    try:
        use_case.execute(product_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/related_products/{product_id}", response_model=List[RelatedProduct])
def get_related_products(
    product_id: str,
    use_case: GetRelatedProductsUseCase = Depends(get_related_products_use_case)
):
    try:
        related_products = use_case.execute(product_id)
        return related_products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/questions/{product_id}", response_model=Question)
def save_questions(
    product_id: str,
    payload: QuestionPayload,
    use_case: SaveProductQuestionsUseCase = Depends(save_questions_use_case)
):
    try:
        question = use_case.execute(product_id, payload.question_text)
        return question
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))