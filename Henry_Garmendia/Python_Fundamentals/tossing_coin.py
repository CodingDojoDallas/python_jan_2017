import random

#ASSIGNMENT: COIN TOSSES

'''
You're going to create a program that simulates tossing a coin 5,000 times. Your program should display how many times the head/tail appears.

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

<<<<<<< HEAD
=======
>>>>>>> upstream/master
def tossing_coin():	
	heads = 0
	tails = 0
	for count in range(1, 5000):
		coin_toss = round(random.random())
		if 0.0 == coin_toss:
			heads += 1
			print 'Attempt #{} Throwing a coin... it\'s head!...Got {} head(s) so far and {} tail(s) so far'.format(count, heads, tails)
		else:
			tails += 1
			print 'Attempt #{} Throwing a coin... it\'s tail!...Got {} head(s) so far and {} tail(s) so far'.format(count, heads, tails)
	print 'Ending the program, Thank you!'

<<<<<<< HEAD
tossing_coin()
=======
tossing_coin()

>>>>>>> upstream/master