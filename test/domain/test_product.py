from src.domains.product import Product


def test_should_create_product():
    product: Product = Product(name="ps5", description="sapato", price="1000")
    print(product.model_dump())
    
    assert product.name == "ps5"
    assert product.description == "sapato"
    assert product.price == 1000