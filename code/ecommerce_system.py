# ecommerce_system

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.orders = []

    def create_order(self, order):
        self.orders.append(order)


class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock


class Order:
    def __init__(self, order_id, user, products):
        self.order_id = order_id
        self.user = user
        self.products = products  
        self.status = "pending"
        self.total_amount = sum([product.price for product in products])

    def complete_order(self):
        self.status = "completed"


class Payment:
    def __init__(self, payment_id, order, amount, payment_status):
        self.payment_id = payment_id
        self.order = order
        self.amount = amount
        self.payment_status = payment_status

    def process_payment(self):
        if self.amount == self.order.total_amount:
            self.payment_status = "successful"
            self.order.complete_order()
        else:
            self.payment_status = "failed"


if __name__ == "__main__":
    user1 = User(1, "John Doe", "john@example.com")
    user2 = User(2, "Jane Doe", "jane@example.com")

    product1 = Product(101, "Laptop", 1000, 10)
    product2 = Product(102, "Smartphone", 500, 20)

    order1 = Order(1001, user1, [product1, product2])

    payment1 = Payment(2001, order1, 1500, "pending")
    payment1.process_payment()

    print(f"Order Status: {order1.status}")
    print(f"Payment Status: {payment1.payment_status}")
