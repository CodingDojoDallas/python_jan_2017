'''
Create a program that simulates tossing a coin 5,000 times. Your program should display how many times the head/tail appears.

Sample output should be like the following:

          Starting the program...

		Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far 
		Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far 
		Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far 
		Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
		........
		Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far 

		Ending the program, thank you!
'''


heads = 0
tails = 0

for i in range(1,5001):
	import random
	random_number = round(random.random())

	if random_number == 0:
		heads += 1
		print "Attempt #", i, "Throwing a coin... It's heads!...", "You have tossed", heads, "head(s) and", tails, "tail(s) so far"
	else:
		tails += 1
		print "Attempt #", i, "Throwing a coin... It's tails!...", "You have tossed", heads, "head(s) and", tails, "tail(s) so far"
print 'Ending the program, thank you!'


