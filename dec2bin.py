# Main function to create binary from decimal input. Function takes input float
# and divides by 2. If the answer is even, the least significant bit (which will be the
# first bit in the list) is 0. If answer is odd, the LSB is 1.
# Note if answer is odd, we must round down using int, and convert back to float to keep
# looping.
def create(num):
	while num > 0:
		if num/2 == int(num/2):
			binlist.append('0')
			num = num/2
		else:
			binlist.append('1')
			num = float(int(num / 2))


# Function to create binary list and also to check if the original number entered
# is zero. If not proceed to function create.
def convert(num):
	global binlist
	binlist = []
	
	if num == 0:
		print 0
	elif num < 0:
		raise ValueError, "Please input a positive number"
	else:
		create(num)


num = float(raw_input("> "))

convert(num)

# Print answer which is a sum of all string of bits. The string is then printed in
# reverse for correct binary conversion.
print ''.join(binlist)[::-1]
