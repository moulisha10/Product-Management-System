import os

class Product:
    def __init__(self, product_id, name, price, description):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description

    def display_product_info(self):
        print(f"Product: {self.name} (ID: {self.product_id})")
        print(f"Price: ${self.price}")
        print(f"Description: {self.description}")
        print("-" * 30)

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product):
        self.shopping_cart.add_product(product)

    def view_cart(self):
        self.shopping_cart.display_cart()

    def checkout(self):
        order = Order(self.shopping_cart)
        self.shopping_cart.clear_cart()
        return order

class Order:
    order_id = 0

    def __init__(self, cart):
        Order.order_id += 1
        self.order_id = Order.order_id
        self.products = cart.products
        self.total_amount = cart.calculate_total()

    def display_order_details(self):
        print(f"\nOrder ID: {self.order_id}")
        print("Products Purchased:")
        for product in self.products:
            print(f"- {product.name}")
        print(f"Total Amount: ${self.total_amount}")
        print("=" * 40)

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_cart(self):
        if not self.products:
            print("Your shopping cart is empty.")
        else:
            print("\nYour Shopping Cart:")
            for product in self.products:
                product.display_product_info()

    def clear_cart(self):
        self.products = []

    def calculate_total(self):
        return sum(product.price for product in self.products)

class ECommerceSite:
    def __init__(self):
        self.products = [
            Product(1, "Laptop", 1200, "Powerful laptop with high-performance specs."),
            Product(2, "Phone", 800, "Smartphone with advanced features."),
            Product(3, "Headphones", 150, "Noise-canceling headphones with great sound quality."),
        ]
        self.customers = []
        self.orders = []

    def register_customer(self):
        """Register a new customer with a unique ID."""
        name = input("Enter your name: ")
        email = input("Enter your email: ")

        # Generate unique customer ID
        customer_id = len(self.customers) + 1
        customer = Customer(customer_id, name, email)
        self.customers.append(customer)

        print(f"Registration successful! Your Customer ID is {customer_id}")

    def add_customer(self, customer):
        self.customers.append(customer)

    def list_products(self):
        print("\nAvailable Products:")
        for product in self.products:
            product.display_product_info()

    def process_order(self, customer):
        order = customer.checkout()
        self.orders.append(order)
        return order

    def get_customer_by_id(self, customer_id):
        """Retrieve customer by ID."""
        return next((c for c in self.customers if c.customer_id == customer_id), None)

def main():
    ecommerce_site = ECommerceSite()

    while True:
        print("\n=== Welcome to the E-Commerce Site! ===")
        print("1. Register as Customer")
        print("2. List Products")
        print("3. Add Product to Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            ecommerce_site.register_customer()

        elif choice == '2':
            ecommerce_site.list_products()

        elif choice == '3':
            customer_id = int(input("Enter your Customer ID: "))
            customer = ecommerce_site.get_customer_by_id(customer_id)
            if customer:
                product_id = int(input("Enter the Product ID to add to cart: "))
                product = next((p for p in ecommerce_site.products if p.product_id == product_id), None)
                if product:
                    customer.add_to_cart(product)
                    print(f"{product.name} added to your cart.")
                else:
                    print("Product not found.")
            else:
                print("Customer not found. Please register first.")

        elif choice == '4':
            customer_id = int(input("Enter your Customer ID to view your cart: "))
            customer = ecommerce_site.get_customer_by_id(customer_id)
            if customer:
                customer.view_cart()
            else:
                print("Customer not found. Please register first.")

        elif choice == '5':
            customer_id = int(input("Enter your Customer ID to checkout: "))
            customer = ecommerce_site.get_customer_by_id(customer_id)
            if customer:
                if customer.shopping_cart.products:
                    order = ecommerce_site.process_order(customer)
                    print("\nOrder placed successfully!")
                    order.display_order_details()
                else:
                    print("Your cart is empty! Please add items before checkout.")
            else:
                print("Customer not found. Please register first.")

        elif choice == '6':
            print("Thank you for shopping with us! Goodbye! 😊")
            break

        else:
            print("Invalid choice. Please enter a number between 1-6.")

if __name__ == "__main__":
    main()
