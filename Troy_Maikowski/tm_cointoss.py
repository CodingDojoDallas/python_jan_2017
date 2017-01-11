import random

def coin_toss():
    tosses = 1
    heads = 0
    tails = 0
    while tosses <= 5000:
        rand_num = round(random.random())
        if rand_num == 1:
            heads += 1
            outcome = "head"
        else:
            tails += 1
            outcome = "tail"
        print "Attempt #" + str(tosses) + ": Throwing a coin... It's a " + outcome + "! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far."
        tosses += 1
        
coin_toss()
        
        