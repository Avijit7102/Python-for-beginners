"""
Problem:
Write a program that asks the user for a positive integer n. Calculate and print the product of the
integers 1 through n.

"""

num = input("Enter a positive integer: ")

if not num.isdigit() or int(num) <= 0:
    print("Enter a positive integer correctly: ")
else:
    n = int(num)
    i = 1
    productTotal = 1
    while i <= n:
        productTotal *= i
        i += 1
    print("The product of the integer: ", productTotal)