"""
Problem:
Write a program that inputs a three digit integer n (no zero in the units position) and returns the digits
of n in reverse order. Your program should reject (politely) any input not in the appropriate range.
For example if you enter the integer 123, the program should output the digits 321 one next to the
other.

Pseudocode / Thinking:
Input: Ask the user to enter a number.

Validation:

1) Must be a number (use .isdigit()).

2) Must be 3 digits long: 100 <= n <= 999.

3) Last digit must not be zero (i.e., n % 10 != 0).

Reverse the digits:

1) Convert to string and reverse it using slicing, or

2) Use integer math (better for this case).

Output the reversed digits as a number.

"""

num = input("Enter a 3-digit number: ")
if not num.isdigit():
    print(f"{num} does not look like a number")
else:
    n = int(num)
    if n < 100 or n > 999:
        print("Please enter a 3-digit number")
    elif n % 10 == 0:
        print("The unit digit can not be a zero")
    else:
        hundreds = n // 100
        tens = (n // 10) % 10
        units = n % 10

        reversed_number = (units * 100) + (tens * 10) + hundreds

        print(f"Reversed Number: {reversed_number}")
