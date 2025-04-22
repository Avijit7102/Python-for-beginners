"""
Problem:
Write a program that asks the user for a positive integer n. It then prints the numbers n down to 1,
one per line.

"""

num = input("Enter a positive integer: ")
if not num.isdigit():
    print("Please enter a number using digits only.")
else:
    n = int(num)
    if n <= 0:
        print("Please enter a number greater than zero.")
    else:
        while n > 0:
            print(n)
            n -= 1
