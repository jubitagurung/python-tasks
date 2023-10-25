def calculate_discounted_price(original_price, discount_percentage):
    discounted_price = original_price - (original_price * discount_percentage / 100)
    return discounted_price

def apply_discount(original_price, discount_percentage):
    discounted_price = calculate_discounted_price(original_price, discount_percentage)
    return f"Discounted Price: ${discounted_price:.2f}"

def shopping_cart(original_price, discount_percentage):
    message = apply_discount(original_price, discount_percentage)
    print(message)

# Test the function
shopping_cart(50, 20)
