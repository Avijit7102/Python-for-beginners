"""
Write a program that will calculate a worker’s pay given the number of hours worked and the rate per
hour. Both values could be floats, for example if someone worked 35.5 hours at a rate of $35.75 an
hour. Work through the example above.

"""

hours = float(input("Enter hours Worked: "))
rate = float(input("Enter hourly rate: "))

pay = hours * rate

print(f"Total Pay: ${pay:.2f}")