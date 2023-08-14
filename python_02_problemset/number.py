#!/usr/bin/env python3
import sys

x = int(sys.argv[1])

if x > 0:
	if x < 50:
		if x % 2 == 0:
			message = 'it is an even number that is smaller than 50'
		else:
			message = 'it is an uneven number that is smaller than 50'
	elif x>50:
		if x % 3 == 0:
			message = 'it is larger than 50 and divisible by 3'
		else:
			message = 'it is larger than 50 and cannot be devided by 3'
	else:
		message = 'number is 50'
elif x < 0:
	message = 'negative'
else:
	message = 'zero'
print(message)
