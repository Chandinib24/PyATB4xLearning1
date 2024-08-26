"""
Task 7 - Leap year checker
Create a program that determines whether a given year is a leap year.

A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

Use an if-else statement to make this determination.
"""

Year=int(input("Enter any of the Year: \n"))
if(Year % 4 == 0 and Year % 100 != 0) or Year % 400 == 0:
    print(f"{Year},This is a leap year")
else:
    print(f"{Year},This is not a leap year")