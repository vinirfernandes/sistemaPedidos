from src.services.customer_service import CustomerService
from src.services.base import ServiceBase
from src.datalayer.base import RepositoryInterface
from src.datalayer.repositories.mock.customer_repository_mock import (CustomerRepositoryMock)


class CustomerFactory:
    @staticmethod
    def create_mock():
        repository: RepositoryInterface = CustomerRepositoryMock()
        service: ServiceBase = CustomerService(repository = repository)
        return service
