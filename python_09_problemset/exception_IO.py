#!/usr/bin/env python3
import sys
import re

# This script reads in a FASTA file and stores each FASTA record separately for easy access for future analysis
# create a FASTA parser using regular expressions
# make sure your parser can deal with a sequence that is split over many lines

fasta_input = ''

pattern = r"^>(\S+)\s+(.*)"
fastaDict = {}
sequence = ''

try:
	fasta_input = sys.argv[1]
	print("User provided file:" , fasta_input)
	file_extension = (".fa", ".fasta")
	if not fasta_input.endswith(file_extension):
		raise ValueError("Not a FASTA file")
	with open(fasta_input, "r") as fasta_object:
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
#		print(line)

except IndexError:
	print("Please provide a file name")
except ValueError:
	print("File needs to be a FASTA file and end with .fa or .fasta")
except IOError as ex:
	print("Can't find file:" , fasta_input, ": ", ex.strerror)


#pattern = r"^>(\S+)\s+(.*)"
#fastaDict = {}
#sequence = ''
#with open(fasta_input, "r") as fasta_object:
#	for line in fasta_object:
#		line = line.rstrip()
#		matches = re.match(pattern,line)
#		if matches:
#			if sequence:	
#				fastaDict[seqID] = sequence
#				seqID = matches.group(1)
#				sequence = ''
#			else:
#				seqID = matches.group(1)
#				sequence = ''
#		else:
#			sequence += line
#	fastaDict[seqID] = sequence
#
#for seqID in fastaDict:
#	print(seqID, fastaDict[seqID], sep='\t')
