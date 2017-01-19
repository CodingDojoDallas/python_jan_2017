'''
Create a function that counts from 1 to 2000. 

As it loops through each number, have your program generate the number and specify whether it's an odd or even number.
'''

def evenandodd():	
	for num in range(1,2001):
		if num % 2 == 0:
			print "Number is", num, "This is an even number."
		else:
			print "Number is", num, "This is an odd number."
evenandodd()