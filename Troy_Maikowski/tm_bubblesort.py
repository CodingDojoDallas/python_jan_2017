from datetime import datetime
import random

a = []

for x in range(3000):
    a.append(round(random.random()*10000))

def bubble_sort(arr):
    start_time = datetime.now()
    print "Start Time:", start_time
    length = len(arr) - 1
    good = False
    
    while not good:
        good = True
        for x in range(length):
            if arr[x] > arr[x+1]:
                good = False
                arr[x], arr[x+1] = arr[x+1], arr[x]
    end_time = datetime.now()
    print "End Time:", end_time
    print "Running Time:", end_time - start_time
    return a

bubble_sort(a)