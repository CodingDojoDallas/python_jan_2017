from datetime import datetime
import random

a = []

for x in range(10000):
    a.append(round(random.random()*10000))
    
print "!!!!!!!!!!!"
print a
print "!!!!!!!!!!!"

def selection_sort(a):
    start_time = datetime.now()
    for x in range(len(a)):
        min_num = min(a[x:])
        min_index = a[x:].index(min_num)
        a[x + min_index] = a[x]
        a[x] = min_num
    end_time = datetime.now()
    print "Running Time:", end_time - start_time
    return a

selection_sort(a)
        