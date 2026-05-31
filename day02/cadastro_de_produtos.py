#!/usr/bin/env python3
"""Product registration example.
"""
__version__ = "1.0"
__author__  = "Alexandre Souza"

product = {
    "name": "Pen",
    "price": 2.50,
    "colors": ["blue", "black", "red"],
    "stock": 100,
    "category": "School Supplies",
    "code": "C12345",
    "description": "Blue ballpoint pen, ideal for everyday writing.",
    "manufacturer": "Faber-Castell",
    "weight": 0.02,
    "dimensions": {
        "length": 14.0,
        "width": 1.0,
        "height": 1.0
    }
}

customer = {
    "name": "Alexandre Souza"
}
purchase = {
    "customer": customer["name"],
    "product": product["name"],
    "quantity": 10,
    "unit_price": product["price"],
}
# Calculate the total amount for the purchase
purchase["total"] = purchase["quantity"] * purchase["unit_price"]
# Display purchase summary
print(f"Customer {purchase['customer']} bought {purchase['quantity']} units of {purchase['product']} at R${purchase['unit_price']:.2f} each. Total: R${purchase['total']:.2f}.")