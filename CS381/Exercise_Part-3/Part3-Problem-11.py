"""
Problem:
Recall the definition of a prime number:
An integer greater than one is called a prime number if its only positive divisors (factors) are one
and itself.
Write a program that inputs a positive integer n and determines if n is prime or composite (i.e.
not a prime).

"""

num = input("Enter a positive number: ")
if not num.isdigit() or int(num) <= 1:
    print("Please enter an integer greater than 1.")
else:
    n = int(num)
    isPrime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            isPrime = False
        i += 1

    if isPrime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")