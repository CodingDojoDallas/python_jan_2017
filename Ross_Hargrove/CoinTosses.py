import random

# These variables keep track of number of times each side is landed on
heads = 0
tails = 0

# Loop for the number of attempts
for toss in range (1,5001):
    # Generates rounded random number
    randomNum = random.random()
    randomRounded = round(randomNum)
    # Conditional that prints statement if heads is landed on
    if randomRounded==0:
        heads+=1
        print "Attempt #{}: Throwing a coin...{}...Got {} head(s) so far and {} tail(s) so far".format(toss, "It's a head!", heads, tails)
    # Conditional that prints statement if tails is landed on
    else:
        tails+=1
        print "Attempt #{}: Throwing a coin...{}...Got {} head(s) so far and {} tail(s) so far".format(toss, "It's a tail!", heads, tails)