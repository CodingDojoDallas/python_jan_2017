'''
Part I

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

x = [4,6,1,3,5,7,15]

def draw_stars(numbers):
	i = 0 # iteration starts at 0

	if len(numbers) < 1: # 7 is not less than 1
		print 'Invalid list'
		return
	
	while i <= len(numbers) - 1: # 0 is equal or less than 6
		print '*' * numbers[i] # should print * multiplied numbers(0) or 4 times. 
		i += 1 # the iternation will increase by 1 and the process starts again

draw_stars(x)




