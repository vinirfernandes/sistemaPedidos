
from src.domains.customer import Customer


def test_should_create_customer():
    customer: Customer = Customer(name="vinicius", email="vini@vini.com")
    print(customer.model_dump())

    assert customer.name == "vinicius"
    assert customer.email == "vini@vini.com"