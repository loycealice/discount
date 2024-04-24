def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage (0 to 100).

    Returns:
        float: The final price after applying the discount, or the original price
        if the discount is less than 20%.
    """
    # Convert discount_percent to a decimal value
    discount = discount_percent / 100
    
    # Apply discount if discount is 20% or higher
    if discount >= 0.2:
        return price * (1 - discount)
    else:
        return price

    # Get user input for original price and convert to float
    original_price = float(input("Enter the original price of the item: "))

    # Get user input for discount percentage and convert to float
    discount_percent = float(input("Enter the discount percentage (0 to 100): "))

    # Calculate the final price after applying the discount
    final_price = calculate_discount(original_price, discount_percent)

    # Print the final price in a formatted manner
    print(f"Final price after applying {discount_percent:.1f}% discount: ${final_price:.2f}")

