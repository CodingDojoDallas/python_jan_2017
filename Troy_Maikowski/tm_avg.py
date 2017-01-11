a = [1,2,5,10,255,3]

def avg(arr):
    total = 0;
    for num in arr:
        total += num
    print total / len(arr)
    
avg(a)