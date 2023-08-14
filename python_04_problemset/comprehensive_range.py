#!/usr/bin/env python3

# write a script that uses list comprehension to print out every number between 0-99 and 1-100
# use range() in a for loop

count99 = [i for i in range(101) if i < 100]
count100 = [i for i in range(101) if i > 0]

for i in count99:
	print(i)

for i in count100:
	print(i)

