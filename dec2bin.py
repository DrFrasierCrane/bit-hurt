def dec2bin(num):	
	if num == 0:
		print 0
	elif num < 0:
		raise ValueError, "Please input a positive integer!"
	else:
		binlist = []
	
		while num > 0:
			binlist.insert(0, num % 2)
			num = num / 2
		
		binlist = int(''.join(str(i) for i in binlist))
		print "Binary number is:", binlist

num = int(raw_input("Please input decimal: "))

convert(num)