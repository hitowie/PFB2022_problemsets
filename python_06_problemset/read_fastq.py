#!/usr/bin/env python3

# count number of lines and number of characters per line in fastq
# report total number of lines, total number of characters, and average line length
with open("Python_06.fastq", "r") as fastq_read:
##	num_lines = sum(1 for line in fastq_read)
	num_lines = 0
	num_char = 0
	for line in fastq_read:
		line = line.rstrip()
		num_lines += 1
		num_char += len(line)

print(f"""total number of lines: {num_lines} 
total number of characters: {num_char} 
average line length: {num_char/num_lines}""")

