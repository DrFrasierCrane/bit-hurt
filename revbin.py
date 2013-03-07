def start(num):
	''' Begins the process by checking input 'num' is a positive, non-zero
		integer '''
	if num == 0:
		print 0
	elif num < 0:
		raise ValueError, "Please input a positive integer!"
	else:
		revbin(num)


def revbin(input):
	''' Converts decimal to binary and reverses the value
		INPUT: Decimal integer
		OUTPUT: Reversed binary'''
	binlist = []

	while input > 0:
		binlist.insert(0, input % 2)
		input /= 2

	new = []

	for i in range(len(binlist)):
		new.append(binlist[i] * 2 ** i)

	return sum(new)