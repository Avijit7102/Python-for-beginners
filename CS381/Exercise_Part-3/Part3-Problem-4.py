"""
Write a program that asks the user for a positive integer n. Print a triangle of “stars”( = “*”) like
in the example below.

"""

num = int(input("Enter a positive integer: "))
i = 1
while i <= num:
    print("*" * i)
    i += 1


print("######### Another Program ############")


j = 1
while num >= j:
    print("*" * num)
    num -= 1
