"""
Problem:
Write a program that asks the user for a positive integer n (>= 2). It then prints the even numbers in
the range 1 to n, one per line.

"""

num = input("Enter a postive number: ")
if not num.isdigit():
    print("Please enter a nubmer using digit only")
else:
    n = int(num)
    if not n >= 2:
        print("Please enter a number greater than or equal to 2.")
    else:
        i = 1
        while i <= n:
            if i % 2 == 0:
                print(i)
            i += 1