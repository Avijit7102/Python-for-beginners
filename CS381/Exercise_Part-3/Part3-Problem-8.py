"""
Problem:
Write a program to request and validate a password from your user. A valid password
will be any two digit integer, both digits of which are even.
Give the user three chances to enter a correct password.
• At each incorrect attempt, print “Invalid password. Try again”
• If the password entered is correct print “Correct! You may access the system.” Exit the
program.
• If the password entered is incorrect print “Too many invalid attempts. Please try again
later.”

"""

i = 1
while i <= 3:
    password = input("Please enter your two digit password: ")
    if not password.isdigit() or not (10 <= int(password) <= 99):
        print("“Invalid password. Try again”")
    else:
        num = int(password)
        tens = num // 10
        ones = num % 10

        if (tens and ones) % 2 == 0:
            print("Correct! You may access the system.")
            break
        else:
            print("“Invalid password. Try again”")

    i += 1
    if i > 3:
        print("Too many invalid attempts. Please try again later.")




