def ccc(a,m):
	for i in range (0, len(a)):
		a[i] *= m
	return a

print ccc([2, 4, 6, 7], 5)