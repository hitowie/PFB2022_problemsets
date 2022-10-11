#!/usr/bin/env python3
import sys

x = int(sys.argv[1])

if x > 0:
	message = 'positive'
	print(message)
elif x < 0:
	message = 'negative'
	print(message)
else:
	message = 'zero'
	print(message)

