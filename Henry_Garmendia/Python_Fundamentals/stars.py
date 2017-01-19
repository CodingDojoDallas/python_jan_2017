#ASSIGNMENT: STARS

#Part 1
'''
Create a function called  draw_stars() that takes a list of numbers and prints out  *.

For example:

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x) should print the following in when invoked:

**** 
****** 
* 
*** 
***** 
******* 
*************************
'''

#Part 2
'''
Modify the function above. Allow a list containing integers and strings to be passed to the  draw_stars() function. 
When a string is passed, instead of  displaying *, display the first letter of the string according to the example below. 
You may use the .lower() string method for this part.

For example:

 x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x) should print the following in the terminal:

**** 
ttt 
* 
mmmmmmm 
***** 
******* 
jjjjjjjjjj
'''

def draw_starts(letterNum):
	#create a loop to iterate throught the list
	for i in range(len(letterNum)):
		#this will check if the list is an integer
		if type(letterNum[i]) == int:
			print '* '*letterNum[i]
		else:
			#this will compute otherwise
			print letterNum[i][0].lower() * len(letterNum[i]) 


draw_starts([1, 3, 5, 8, "Coding", 3, "Dojo", 4, 15, "Ninja Style", 6, 4 ])