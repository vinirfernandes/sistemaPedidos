from src.datalayer.base import RepositoryInterface
from src.domains.customer import CustomerRegistration, Customer


class CustomerRepositoryInterface(RepositoryInterface):
    async def register(self, customer_registration: CustomerRegistration) -> Customer:
        raise NotImplementedError

    async def email_already_exist(self, email: str) -> bool:
        raise NotImplementedError