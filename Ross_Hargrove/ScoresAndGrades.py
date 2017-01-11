print "Scores and Grades"

# function that determines grade from score
def myGrade(a):
    if a <= 100 and a >= 90:
        print "Your grade is A"
    elif a <= 89 and a >= 80:
        print "Your grade is B"
    elif a <= 79 and a >= 70:
        print "Your grade is C"
    elif a <= 69 and a >= 60:
        print "Your grade is D"

# loop that prompts user for score
for count in range (0,10):
    print "Score:",
    myGrade(input())

print "End of the program. Bye!"

