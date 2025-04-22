"""
Problem:
Write a program that asks the user for a positive integer n where the right-most digit is not a
zero. Construct and output the integer whose digits are the reverse of those in n.
For example, if n has the value 123, then you need to construct the integer 321. Note you are not
just printing the digits of n in reverse order; you are actually constructing the new integer.
Answer:
1. What is the algorithm (method)?
Answer:

1) Input Validation

* Ask the user for a positive integer n.

* Make sure it's:

* A positive number (> 0)

* The last digit is not zero (you can check with n % 10 != 0).

2) Initialize a variable to hold the reversed number — for example, reversedNum = 0.

3) Loop while n > 0:

* Get the last digit using digit = n % 10.

* Add this digit to the reversed number by shifting digits left:
* reversedNum = reversedNum * 10 + digit

* Remove the last digit from n:
    n = n // 10

When the loop ends, reversedNum is your final result.

Print or return the reversed number.
"""

num = input("Enter a positive number: ")
if not num.isdigit() or int(num) < 0 or num[-1] == '0':
    print("Enter a positive integer correctly where the last digit is not zero.")
else:
    n = int(num)
    reversedNumber = 0
    while n > 0:
        lastDigit = n % 10
        reversedNumber = reversedNumber * 10 + lastDigit
        n = n // 10

    print("Reversed Number: ", reversedNumber)


