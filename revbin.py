# Code written by Tyler Sartin #

def revbin(n):
	''' Converts decimal to binary and reverses the value
		INPUT: Decimal integer
		OUTPUT: Reversed binary'''
	if n == 0:
		print 0
	elif n < 0:
		raise ValueError, "Please input a positive integer."
	else:
		n = int(n)
		binlist = []

		while n > 0:
			binlist.insert(0, n % 2)
			n /= 2

		new = []

		for i in range(len(binlist)):
			new.append(binlist[i] * 2 ** i)

		return sum(new)
