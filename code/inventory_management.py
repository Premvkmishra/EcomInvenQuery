# inventory_management

class Product:
    def __init__(self, product_id, name, stock):
        self.product_id = product_id
        self.name = name
        self.stock = stock

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
        else:
            raise ValueError(f"Not enough stock for product {self.name}")


def process_orders(products, sales_orders):
    for order in sales_orders:
        product = next((p for p in products if p.product_id == order["product_id"]), None)
        if product:
            try:
                product.reduce_stock(order["quantity"])
                print(f"Processed order for {product.name}")
                if product.stock < 10:
                    print(f"Alert: {product.name} stock is below threshold. Needs restocking!")
            except ValueError as e:
                print(e)
        else:
            print(f"Product with ID {order['product_id']} not found.")


def restock_items(products, restock_list):
    for restock in restock_list:
        product = next((p for p in products if p.product_id == restock["product_id"]), None)
        if product:
            product.stock += restock["quantity"]
            print(f"Restocked {product.name} with {restock['quantity']} units.")
        else:
            print(f"Product with ID {restock['product_id']} not found.")


# Example usage
if __name__ == "__main__":
    products = [
        Product(101, "Laptop", 15),
        Product(102, "Smartphone", 8),
        Product(103, "Tablet", 12)
    ]

    
    sales_orders = [
        {"product_id": 101, "quantity": 5},
        {"product_id": 102, "quantity": 4},
        {"product_id": 103, "quantity": 3}
    ]

    process_orders(products, sales_orders)

    restock_list = [
        {"product_id": 102, "quantity": 20}
    ]
    restock_items(products, restock_list)
