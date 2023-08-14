#!/usr/bin/env python3
import re

# using pattern matching, find all the header lines in fasta file
# if a line matches the format of a FASTA header, extract sequence name and description using sub patterns (groups)

pattern = r"^>(\w+)\s?(.*)"

with open("Python_07.fasta", "r") as fasta_read:
	for line in fasta_read:
		line = line.rstrip()
		header = re.findall(pattern, line)
		if len(header) > 0:
			for (seqID, descr) in header:
				print(f"id: {seqID} descr: {descr}")

