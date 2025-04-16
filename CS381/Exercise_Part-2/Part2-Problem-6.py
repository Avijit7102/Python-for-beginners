"""
Problem:
Write a program that asks the user to enter two integers. Your program should:
• “Store” the values entered in variables a and b.
• “Print a and b.
• “Swap” the values in a and b, so that what was in a is now in b and vice versa.
• Print a and b. At this point the values should be the reverse of what you printed above.
Answer:

Will this one work?
Answer: Yes, the program will work if you use either the traditional swapping method or Python's unpacking feature.


How about this?

Note: Python allows a more direct way to do this using “unpacking.” Here is how:
a, b = b, a


How come this works?
This works because of tuple unpacking in Python:
The right-hand side b, a is packed into a tuple: (b, a)

Python then unpacks the tuple on the left-hand side into a and b

This happens simultaneously, so no values are overwritten in the process

"""

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))


print("Before swapping: ")
print("a: ", a)
print("b: ", b)

# Swap using unpacking
a, b = b, a

print("After swapping: ")
print("a: ", a)
print("b: ", b)
