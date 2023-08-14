#!/usr/bin/env python3

numbers = [101,2,15,22,95,33,2,27,72,15,52]

# iterate through each element of numbers using `for` loop
# print out only even values

for n in numbers:
	if n%2 == 0:
		print(n)

# sort numbers, calculate and print cumulative sums of even and odd values

even = []
odd = []

for n in numbers:
	if n%2 == 0:
		even.append(n)
	else:
		odd.append(n)
print(f"""Sum of even numbers: {sum(even)}
Sum of odds: {sum(odd)}""")
 
