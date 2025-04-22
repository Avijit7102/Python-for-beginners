"""
Problem:
Write a program that asks the user for a positive integer n. It then prints the numbers 1 through n, one
per line.

"""

num = input("Enter a positive integer: ")
if not num.isdigit():
    print("Please enter a nubmer using digit only")
else:
    n = int(num)
    if n <= 0:
        print("please enter a number grater than zero")
    else:
        i = 1
        while i <= n:
            print(i)
            i += 1