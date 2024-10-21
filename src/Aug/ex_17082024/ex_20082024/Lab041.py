#Grade calculator
#Write a program that calculates and displays the letter grade for
# a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
#input- score - 89
#output- B

#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59

#Logic building formula

#1.user inputs-score-integer
#2.0/p--> str--like grade A,B etc
# Rough logic

score=int(input("Enter the score\n"))
Grade="F"

if 90 <= score <= 100:  #simplified chaining format-- 90<= score <=100
    print("Your grade is", "A")
elif score >= 80 and score <=89:  # simplified chaining format-- 80<= score <=89
        print("Your grade is", "B")
elif score >= 70 and score <= 79:  # simplified chaining format-- 70<= score <=79
        print("Your grade is", "C")
elif score >= 60 and score <= 69:  # simplified chaining format-- 60<= score <=69
        print("Your grade is D" )
else:
    print("Your grade is", "F")