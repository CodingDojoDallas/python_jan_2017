#ASSIGNMENT: AVERAGE LIST

'''
Create a program that prints the average of the values in the list:
'''

a = [1, 2, 5, 10, 255, 3]
total = 0

for i in a:
	total += i

print total/len(a)
