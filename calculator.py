def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

# prompt for input
price = float(input("Enter original price of item: "))
discount_percent = float(input("Enter the discount percentage: "))

# final price calculation 
final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20: 
    print(f"Final price after discount: ${final_price:2f}")
else:
    print(f"No discount applied. Original Price: ${price:2f}")