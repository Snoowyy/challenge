import pytest
from app.core.domain.product_model import Product
from app.core.infrastructure.adapters.json_product_repository import JSONProductRepository

@pytest.fixture
def json_product_repository():
    return JSONProductRepository()

def test_get_all_products(json_product_repository):
    products = json_product_repository.get_all()
    assert len(products) == 1

def test_get_product(json_product_repository):
    product = json_product_repository.get_by_id("A55-256-BLUE")
    assert product.id == "A55-256-BLUE"

def test_save_product(json_product_repository):
    product = Product(id="TEST-PRODUCT", product_info=Product.ProductInfo(title="Test Product", price=Product.Price(real_amount=100)))
    json_product_repository.save_product(product)
    assert json_product_repository.get_by_id("TEST-PRODUCT").id == "TEST-PRODUCT"

def test_remove_product(json_product_repository):
    product = Product(id="TEST-PRODUCT", product_info=Product.ProductInfo(title="Test Product", price=Product.Price(real_amount=100)))
    json_product_repository.save_product(product)
    json_product_repository.remove_product("TEST-PRODUCT")
    assert json_product_repository.get_by_id("TEST-PRODUCT") is None
