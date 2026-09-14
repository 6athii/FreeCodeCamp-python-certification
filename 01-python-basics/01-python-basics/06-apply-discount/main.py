def apply_discount(price, discount):
    # 3. Check if price is a number (int or float)
    if not isinstance(price, (int, float)) or isinstance(price, bool):
        return "The price should be a number"
        
    # 4. Check if discount is a number (int or float)
    if not isinstance(discount, (int, float)) or isinstance(discount, bool):
        return "The discount should be a number"
        
    # 5. Check if price is greater than 0
    if price <= 0:
        return "The price should be greater than 0"
        
    # 6. Check if discount is between 0 and 100
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
        
    # 7-11: Calculate and return the final price
    final_price = price - (price * (discount / 100))
    return final_price
