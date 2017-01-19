#ASSIGNMENT: SCORES AND GRADES

'''
Create a program that prompts the user ten times for a test score between 60 and 100. Each time a score is generated, 
your program should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A
'''

#the result shoud be like this
'''
Scores and Grades
Score: 87; Your grade is B
Score: 67; Your grade is D
Score: 95; Your grade is A
Score: 100; Your grade is A
Score: 75; Your grade is C
Score: 90; Your grade is A
Score: 89; Your grade is B
Score: 72; Your grade is C
Score: 60; Your grade is D
Score: 98; Your grade is A
End of the program. Bye!
'''

def score_grades():
	#need a loop to for each input and check until value is correct
	print 'Scores and Grades'
	#loop to ask user input 10 times
	i = 0
	while i < 10:
		#ask a user for an input
		scoreNum = raw_input('Please ente a number between (60-100): ')

		try:
			#convert user input into integer and check if string
			scoreNum == int(scoreNum)
		except ValueError:
			print 'Error: {} isn\'t a number. Please enter a number'.format(scoreNum)
		else:
			#loop to check if number is smaller than 60 or greater than 100
			if int(scoreNum) < 60 or int(scoreNum) > 100:
				print 'Error: Incorrect value. Please enter a number between (60-100)'
				continue
			elif int(scoreNum) > 89:
				grade = 'A'
				i += 1
			elif int(scoreNum) > 79:
				grade = 'B'
				i += 1
			elif int(scoreNum) > 69:
				grade = 'C'
				i += 1
			else:
				grade = 'D'
				i += 1
			print 'Score: {}; Your grade is {}'.format(scoreNum, grade)
	print 'End of the program. Bye!'

score_grades()
