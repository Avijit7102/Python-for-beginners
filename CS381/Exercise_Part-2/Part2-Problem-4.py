"""
Problem:
Write a program that asks the user to enter an integer. Your program should “echo” the input and print
True if the number is even and False if the number is odd.

"""

num = int(input("Enter an integer: "))
print("You entered: ", num)
is_even = (num % 2 == 0)
print(is_even)