from src.datalayer.repositories.mock.memdb import CUSTOMER_DB
from src.domains.customer import Customer, CustomerRegistration
from src.datalayer.interfaces.customer_repository_interface import ( CustomerRepositoryInterface )


class CustomerRepositoryMock(CustomerRepositoryInterface):
    async def register(self, customer_registration: CustomerRegistration) -> Customer:
        customer: Customer = Customer(**customer_registration.model_dump())
        CUSTOMER_DB.append(customer)
        return customer


    async def email_already_exist(self, email: str) -> bool:
        email_exists = list(filter(lambda c: c.email == email, CUSTOMER_DB))
        
        return True if len(email_exists) > 0 else False