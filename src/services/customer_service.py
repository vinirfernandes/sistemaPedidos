from dataclasses import dataclass
from src.services.exceptions.customer_exceptions import EmailAlreadyExist
from src.domains.customer import CustomerRegistration, Customer
from src.datalayer.interfaces.customer_repository_interface import CustomerRepositoryInterface
from src.services.base import ServiceBase

@dataclass
class CustomerService(ServiceBase):
    repository: CustomerRepositoryInterface
    
    async def register(self, customer_registration: CustomerRegistration) -> Customer:
        if await self.email_already_exist(customer_registration.email):
            raise EmailAlreadyExist()

        return await self.repository.register(customer_registration)

    async def email_already_exist(self, email: str) -> bool:
        return await self.repository.email_already_exist(email)