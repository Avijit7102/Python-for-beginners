"""
Problem:
Write a program to ask the user their age in years. Your program should calculate and print their age in
seconds.

"""

age = int(input("Enter your age: "))
# 1 year = 365 days, 1 day = 24 hours, 1 hour = 3600 seconds

age_seconds = age * 365 * 24 * 60 * 60
print(f"You are approximately {age_seconds} seconds old")