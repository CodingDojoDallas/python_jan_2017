'''
Create a program that prints all the odd numbers from 1 to 1000. 
Use the for loop and don't use array to do this exercise. 
'''

for odd in range(1,10001):
	if odd % 2 != 0:
		print odd	

# Create another program that prints all the multiples of 5 from 5 to 1,000,000.
for multiples in range(5,1000001):
	if multiples % 5 == 0:
		print multiples