"""
Problem:
We will say that a number is a palindrome if it reads the same forwards and backwards. So:
• 1221 is a palindrome
• 6556 is a palindrome
• 1234 is not a palindrome
Write a program that inputs a four digit integer and determines if the number is a palindrome or not.
Your program should reject (politely) any input not in the appropriate range.

"""

num = input("Enter a 4 digit number: ")

if not num.isdigit():
    print(f"{num} does not look like a number")
elif len(num) != 4:
    print("Please enter exactly 4 digit number")
else:
    if num == num[::-1]:
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")
