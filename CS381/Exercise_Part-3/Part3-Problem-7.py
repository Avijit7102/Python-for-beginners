"""
Problem:
Write a program that asks the user for a positive integer n. Calculate and print the sum of the
odd integers in the range 1 through n.

"""
num = input("Enter a positive integer: ")

if not num.isdigit() or int(num) < 0:
    print("Enter a positive integer correctly: ")
else:
    n = int(num)
    sum = 0
    i = 1
    while i <= n:
        if i % 2 != 0:
            sum += i
        i += 1

    print("The sum of the odd integers: ", sum)
