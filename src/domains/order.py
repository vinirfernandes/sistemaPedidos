from enum import Enum
from uuid import UUID
from pydantic import BaseModel, Field
from src.domains.customer import Customer
from src.domains.base import DomainBase

class OrderStatusName(str, Enum):
    ACCOMPLISHED = "REALIZADO"
    IN_PREPARATION = "EM PREPARÇÃO"
    SENT = "ENVIADO"
    DELIVERED = "ENTREGUE"
    FINISHED = "FINALIZADO"

class OrderStatus(BaseModel):
    name: OrderStatusName = Field(default=OrderStatusName.ACCOMPLISHED)
    
class OrderItem(BaseModel):
    product_id: UUID
    price: float
    quantity: int

class Order(DomainBase):
    customer : Customer
    status: list[OrderStatus] = Field(default=[])
    item: list[OrderItem] = Field(default=[])

    def add_status(self, status: OrderStatus):
        self.status.append(status)
    
    def add_item(self, item: OrderItem):
        self.item.append(item)
    
    def total(self):
        return sum([item.price * item.quantity for item in self.item])