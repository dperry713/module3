def display_orders(orders):
    for customer, product, quantity in orders:
        print(f"Customer: {customer}, Product: {product}, Quantity: {quantity}")

# Sample Order Data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Smartphone", 3)
]

# Display the orders
display_orders(orders)
