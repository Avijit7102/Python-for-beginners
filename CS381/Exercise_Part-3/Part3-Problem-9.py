"""
Problem:
Write a program that asks the user for a positive integer n where the right-most digit is not a
zero. Print out the digits of n from right to left – one next to the other.
Answer:

"""

num = input("Enter a positive integer: ")
if not num.isdigit() or int(num) < 0 or num[-1] == '0':
    print("Enter a positive integer correctly where the last digit is not zero.")
else:
    n = int(num)
    while n > 0:
        lastDigit = n % 10
        print(lastDigit, end="")
        n = n // 10
