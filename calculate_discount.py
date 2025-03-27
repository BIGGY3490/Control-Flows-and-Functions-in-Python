# Function to calculate the final price after applying the discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Main program to prompt user for inputs and display results
# Prompting user for the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculating the final price using the function
final_price = calculate_discount(original_price, discount_percentage)

# Displaying the final price or a message if no discount is applied
if final_price < original_price:
    print(f"The final price after applying the discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {original_price}")
