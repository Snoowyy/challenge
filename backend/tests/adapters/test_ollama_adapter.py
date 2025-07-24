import pytest
from app.core.domain.product_model import RelatedProduct
from app.core.infrastructure.adapters.ollama_adapter import OllamaRelatedProductsAdapter

@pytest.fixture
def ollama_related_products_adapter():
    return OllamaRelatedProductsAdapter()

def test_get_related_products(ollama_related_products_adapter):
    related_products = ollama_related_products_adapter.get_related_products("A55-256-BLUE")
    assert len(related_products) == 3
