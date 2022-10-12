#!/usr/bin/env python3

list = [101,2,15,22,95,33,2,27,72,15,52]
even = []
odd = []

for i in list:
	if i%2 == 0:
		even.append(i)
	else:
		odd.append(i)

print(f"""Sum of even numbers: {sum(even)}
Sum of odds: {sum(odd)}""")
 
