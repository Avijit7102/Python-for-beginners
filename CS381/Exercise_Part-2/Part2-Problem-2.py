"""
Problem:
Write a program that asks the user to enter a temperature in Fahrenheit. Your program should calculate
and print the temperature in Centigrade.

"""
# Formula : C = (F - 32) * 5 / 9

fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

centigrade = (fahrenheit - 32) * 5/9

print(f"Temperature in Centigrade is: {centigrade:.2f}")
