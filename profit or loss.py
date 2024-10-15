'''
4) A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00
'''
ans:
 # Function to calculate profit or loss
def calculate_profit_loss(cost, selling_price):
    # Calculate total selling price for a dozen bananas
    total_selling_price = selling_price * 12
    
    # Calculate profit or loss
    profit_loss = total_selling_price - cost
    
    return profit_loss

# Input format
cost = float(input("Enter total cost (X): "))
selling_price = float(input("Enter selling price per banana (Y): "))

# Calculate profit or loss
result = calculate_profit_loss(cost, selling_price)

# Output format
if result > 0:
    print(f"Profit : Rs.{result:.2f}")
elif result < 0:
    print(f"Loss : Rs.{-result:.2f}")
else:
    print("No Profit No Loss")
