'''
Create a program that prompts the user ten times for a test score between 60 and 100. Each time a score is generated, your program should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A
'''



def reportcard():
	restart = True
	while restart:
		restart = False
		for i in range(1,11):
			print 'Please input a score between 60 and 100'
			user = raw_input()
			score = int(user)

			if score > 101 or score < 60:
				print 'You entered an invalid score\n'
				restart = True
				break
			elif score < 101 and score > 89:
				print 'Score:', score,"Your grade is a A\n"
			elif score < 90 and score > 79:
				print 'Score:', score,"Your grade is a B\n"
			elif score < 80 and score > 69:
				print 'Score:', score,"Your grade is a C\n"
			else:
				print 'Score:', score,"Your grade is a D\n"
	print 'End of the program. Bye!\n'
reportcard()

