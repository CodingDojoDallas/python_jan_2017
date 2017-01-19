#ASSIGNMENT: MULTIPLY

'''
Create a function called 'multiply' that reads each value in the list (e.g. a = [2, 4, 10, 16])
and returns a list where each value has been multiplied by 5.
'''

#Should print [10, 20, 50, 80 ].

def numMulti(a, multiplyer):
	#create a new array to hold new values
	aNew = []
	#create a loop to iterate array
	for i in a:
		#create a temp variable to hold new numbers
		temp = (i * multiplyer)
		#add the item from temp to the end of the list
		aNew.append(temp)
	return aNew

print numMulti([2,4,10,16],5)
