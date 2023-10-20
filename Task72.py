def calculate_discounted_price(original_price, discount_percentage):
    discount_amount = (discount_percentage / 100) * original_price
    discounted_price = original_price - discount_amount
    return discounted_price

def apply_discount(original_price, discount_percentage):
    discounted_price = calculate_discounted_price(original_price, discount_percentage)
    return f"The discounted price is ${discounted_price:.2f}"

def shopping_cart(original_price, discount_percentage):
    message = apply_discount(original_price, discount_percentage)
    print(message)

shopping_cart(50, 20)