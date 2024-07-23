# Sistema de Pedidos

- Customer
    name
    email
        -Cadastrar Cliente
        - Verificar se o email já está cadastrado

- Product
    name 
    description
    price

-Order 
    [OrderStatus]
    [OrdemItem]
    total

-OrderStatus
    name (REALIZADO, EM PREPARACAO, ENVIADO, ENTREGUE, FINALIZADO)

-OrderItem
    - product_id
    - price
    - quantity
