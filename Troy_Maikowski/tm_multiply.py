a = [2,4,10,16]

def multiply(arr, factor):
    new_arr = []
    for num in arr:
        new_arr.append(num * factor)
    return new_arr

print multiply(a,5)