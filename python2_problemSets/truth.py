#!/usr/bin/env python3
import sys

a = sys.argv[1]
# sys.argv will always be class string and bool(str) is always True

if bool(a) == True:
	message = 'True'
	print(message)
else:
	message = 'Not True'
	print(message)

