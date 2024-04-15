# [Open-Closed Principle (OCP)] Download the python file from this link. Suppose we have a Product class that represents a generic product, and we want to calculate the total price of a list of products. Initially, the Product class only has a price attribute, and we can calculate the total price of products based on their prices.

# Now, let's say we want to add a discount feature, where some products might have a discount applied to their prices. To add this feature, we would need to modify the existing Product class and the calculate_total_price function, which violates the Open/Closed Principle. Redesign this program to follow the Open-Closed Principle (OCP) which represents “Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.”


class Product:
    def __init__(self, price):
        self.price = price

    def give_discount(self, discount_percent):
        self.price *= 1 - discount_percent


def calculate_total_price(products):
    total_price = 0
    for product in products:
        total_price += product.price
    return total_price


# Using the calculate_total_price function with a list of products
products = [Product(100), Product(100), Product(100)]
discounts = [0.2, 0.1, 0.5]
print("Total Price before discount:", calculate_total_price(products))

# apply discount
for product, discount in zip(products, discounts):
    product.give_discount(discount)

print("Total Price after discount:", calculate_total_price(products))
