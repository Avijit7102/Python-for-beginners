"""
Problem:
Write a program that asks the user for a positive integer n. Calculate and print the sum of the
integers 1 through n.

"""

num = input("Enter a positive integer: ")

if not num.isdigit() or int(num) <= 0:
    print("Enter a positive integer correctly: ")
else:
    n = int(num)

    i = 1
    sum = 0
    while i <= n:
        sum += i
        i += 1

    print("Sum of the integer is: ", sum)

