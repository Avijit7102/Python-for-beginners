"""
Problem
Write a program to provide change in coins.
Input
Have your program ask the user to input some amount of money.
Output
Your program should output the minimum number of coins required to render the amount entered
into coins. The coins are half-dollars, quarters, dimes, nickels and pennies.
Your program should also list how many of each coin needs to be provided. Each denomination on its own
line, starting with half-dollars.

"""

amount = float(input("Enter an amount in dollars: $"))
cents = round(100 * amount)

coins = {
    "Half-dollars": 50,
    "Quarters": 25,
    "Dimes": 10,
    "Nickels": 5,
    "Pennies": 1
}

print("Minimum number of coins: ")
for coin, value in coins.items():
    count = cents // value
    cents %= value
    print(f"{coin}: {count}")


