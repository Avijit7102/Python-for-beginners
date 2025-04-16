"""
Problem:
Write a program that asks the user to enter an integer. Your program should “echo” the input and print
EVEN if the number is even and ODD if the number is odd.

"""

num = int(input("Enter an integer: "))
print("You entered: ", num)

if num % 2 == 0:
    print("Even")
else:
    print("ODD")