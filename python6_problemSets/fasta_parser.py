#!/usr/bin/env python3

# This script reads in a FASTA file and stores each FASTA record separately for easy access for future analysis

with open("Python_06.fasta", "r") as read_fasta:
	fastaDict = {}
	for line in read_fasta:
		line = line.rstrip()
		if line.startswith(">"): #header line starts with >
	# if line.find(">") ==1:
			header = line # save as dict key, who to remove >?
			fastaDict[header] = ''
		else: #sequence line
			# seq = line
			# fastaDict[header] = seq
			fastaDict[header] += line

print(fastaDict)
