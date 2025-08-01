# Step 1: Define hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135
}

# Step 2: Take user input
portfolio = {}
print("Enter the stocks you own (type 'done' to finish):")

while True:
    stock = input("Stock symbol (e.g., AAPL): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in list. Try again.")
        continue
    try:
        quantity = int(input(f"How many shares of {stock}? "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Step 3: Calculate total investment
total_value = 0
print("\nYour Portfolio:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    print(f"{stock}: {quantity} shares x ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Step 4: Optionally save to file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter filename (with .txt or .csv): ")
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price,Total Value\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock},{quantity},{price},{value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}")
    print(f"✅ Portfolio saved to {filename}")
