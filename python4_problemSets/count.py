#!/usr/bin/env python3
import sys

# write a script that takes the start and end values from the command line and counts from start to end

count = int(sys.argv[1])
end = int(sys.argv[2])

while count <= end:
	if count % 2 != 0:
		print(count)
	count += 1

