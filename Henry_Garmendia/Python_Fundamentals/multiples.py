#ASSIGNMENT: MULTIPLES

#Part 1
'''
Create a program that prints all the odd numbers from 1 to 1000.
Use the for loop and don't use array to do this exercise.
'''

for odd_num in range(1, 1000):
	if odd_num %2 == 1:
		print odd_num

#Part 2
'''
Create another program that prints all the multiples of 5 from 5 to 1,000,000. 
'''

for multi in range(5, 1000000):
	if multi %5 == 0:
		print multi
		