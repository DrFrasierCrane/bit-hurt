def dec2bin(num):
	''' This function takes in a decimal integer and then converts it
		to binary
		INPUT: Decimal integer
		OUTPUT: Binary'''
	num = int(num)	
	if num == 0:
		print 0
	elif num < 0:
		raise ValueError, "Please input a positive integer!"
	else:
		binlist = []

		while num > 0:
			binlist.insert(0, num % 2)
			num /= 2

		binlist = int(''.join(str(i) for i in binlist))
		return binlist