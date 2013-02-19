def convert(num):	
	if num == 0:
		print 0
	elif num < 0:
		raise ValueError, "Please input a positive integer!"
	else:
		binlist = []
	
		while num > 0:
			binlist.append(num % 2)
			num = num / 2
		
		binlist.reverse()
		binlist = int(''.join(str(i) for i in binlist))
		print binlist

num = int(raw_input("> "))

convert(num)