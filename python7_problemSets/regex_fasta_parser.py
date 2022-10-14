#!/usr/bin/env python3
import re

# This script reads in a FASTA file and stores each FASTA record separately for easy access for future analysis
# create a FASTA parser using regular expressions
# make sure your parser can deal with a sequence that is split over many lines

pattern = r"^>(\w+)\s?(.*)"

with open("Python_07.fasta", "r") as read_fasta:
	fastaDict = {}
	for line in read_fasta:
		line = line.rstrip()
		header = re.match(pattern, line)
		if header:
			seqID = header.group(1)
			fastaDict[seqID] = ''
		else:
			fastaDict[seqID] += line

print(fastaDict)
