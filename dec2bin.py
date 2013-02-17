from sys import exit

def create(num):
	while num > 0:
		if num/2 == int(num/2):
			binlist.append('0')
			num = num/2
		else:
			binlist.append('1')
			num = float(int(num / 2))

def convert(num):
	global binlist
	binlist = []
	
	if num == 0:
		print 0
	else:
		create(num)
	
num = float(raw_input("> "))

convert(num)

answer = ''.join(binlist)

print answer[::-1]
