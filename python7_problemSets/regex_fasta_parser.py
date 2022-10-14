#!/usr/bin/env python3
import re

# This script reads in a FASTA file and stores each FASTA record separately for easy access for future analysis
# create a FASTA parser using regular expressions
# make sure your parser can deal with a sequence that is split over many lines

pattern = r"^>(\S+)\s+(.*)"
fastaDict = {}
sequence = ''
with open("Python_07.fasta", "r") as fasta_object:
	for line in fasta_object:
		line = line.rstrip()
		matches = re.match(pattern,line)
		if matches:
			if sequence:	
				fastaDict[seqID] = sequence
				seqID = matches.group(1)
				sequence = ''
			else:
				seqID = matches.group(1)
				sequence = ''
		else:
			sequence += line
	fastaDict[seqID] = sequence

for seqID in fastaDict:
	print(seqID, fastaDict[seqID], sep='\t')
