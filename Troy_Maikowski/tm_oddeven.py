def odd_even():
    for num in range (1,2001):
        output = "Number is " + str(num) + "."
        if num % 2 == 0:
            output += " This is an even number"
        else:
            output += " This is an odd number"
        print output
            
odd_even()