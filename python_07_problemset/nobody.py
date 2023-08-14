#!/usr/bin/env python3
import re

# find every occurence of 'Nobody' and print its position
with open("Python_07_nobody.txt", "r") as read_file:
	line_count = 0
	for line in read_file:
		line = line.rstrip()
		line_count += 1
		matches = re.finditer(r"Nobody", line)
		for match in matches:
			print(f"found 'Nobody' in line {line_count}: {match}")	
		
# substitute every occurence of 'Nobody' with 'Klaus' and write an output file with that name	
with open("Python_07_nobody.txt", "r") as read_file, open("Klaus.txt", "w") as write_file:
	for line in read_file:
		line = line.rstrip()
		new_line = re.sub(r"Nobody", "Klaus", line)
		write_file.write(f"{new_line}\n")
print(f"wrote to file 'Klaus.txt'")
