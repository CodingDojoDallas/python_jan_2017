import random

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

tossing_coin()









