def scores_and_grades():
    for x in range(1,11):
        grade = input("Input a score between 60 and 100:\n")
        if grade > 100:
            print "Invalid grade"
        elif grade >= 90:
            print "Score:", str(grade) + ";", "Your grade is A"
        elif grade >= 80:
            print "Score:", str(grade) + ";", "Your grade is B"
        elif grade >= 70:
            print "Score:", str(grade) + ";", "Your grade is C"
        elif grade >= 60:
            print "Score:", str(grade) + ";", "Your grade is D"
        else:
            print "Invalid grade"
        
scores_and_grades()