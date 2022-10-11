#!/usr/bin/env python3
import sys

x = int(sys.argv[1])

if x > 0:
	if x < 50:
		if x % 2 == 0:
			message = 'is an even number that is smaller than 50'
		else:
			message = 'is an uneven number that is smaller than 50'
	elif x>50:
		if x % 3 == 0:
			message = 'is larger than 50 and divisible by 3'
		else:
			message = 'is larger than 50 and cannot be devided by 3'
	else:
		message = 'is your number'
elif x < 0:
	message = 'is a negative number'
else:
	message = 'is your number'
print(x, message)
