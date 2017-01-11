def multiply(a, b):
    newArr = []
    for place in a:
        newElement = place*b
        newArr.append(newElement)
    return newArr

a = [2,4,10,16]
b = 5

c = multiply(a,b)
print c

