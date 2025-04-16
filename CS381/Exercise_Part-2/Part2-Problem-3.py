"""
Problem:
Given a temperature in Centigrade, write the assignment statement to calculate the temperature in
Fahrenheit. Now, do it the other way, i.e. go from Fahrenheit to Celsius.

"""

# Formula :  °C x 9/5 + 32 = °F

centigrade = float(input("Enter a temperature in Centigrade: "))

fahrenheit = (centigrade * 9/5) + 32

print(f"Temperature in Fahrenheit is: {fahrenheit:.2f}")
