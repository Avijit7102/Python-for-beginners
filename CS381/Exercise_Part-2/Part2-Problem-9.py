"""
Problem:
Write a program using “if – elif” that converts a numerical score to a letter grade according to the
following scheme:
• If the score is 90 or above, the grade is A.
• If the score is between 80 and 90 the grade is B.
• If the score is between 70 and 80 the grade is C.
• If the score is between 60 and 70 the grade is D.
• If the score is less than 60, the grade is F.
In the above, between x and y means starting with x and less than y.
The program prints the score and the associated letter grade.
If the score entered is not in any of the above ranges, the program prints the score and the message
“Score out of Range!”.

"""

score = float(input("Enter your score: "))
grade = None
#condition
if score >= 90:
    grade = 'A'
elif score >= 80 and score < 90:
    grade = 'B'
elif score >= 70 and score < 80:
    grade = 'C'
elif score >= 60 and score < 70:
    grade = 'D'
elif score >= 0 and  score < 60:
    grade = 'F'
else:
    grade = None

if grade is not None:
    print("Score: ", score)
    print("Grade: ", grade)
else:
    print(f"{score} out of Range!")

