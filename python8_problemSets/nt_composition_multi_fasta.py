#!/usr/bin/env python3
import sys
import re

# take a multi FASTA file from user input and calculate nucleotide composition for each sequence
# use a datastructure to keep count
# print out each sequence name and its composition

file_input = sys.argv[1]

pattern = r"^>(\S+)\s+(.*)"
fasta_dict = {}
seqID = ''
seq_descr = ''
sequence = ''
count = ''

with open(file_input, "r") as fasta_object:
	for line in fasta_object:
		line = line.rstrip()
		match = re.match(pattern, line)
		if match:
			if sequence:
				fasta_dict[seqID] = {'sequence' : sequence, 'description' : seq_descr}
				seqID = match.group(1)
				seq_descr = match.group(2)
				sequence = ''
			else:
				seqID = match.group(1)
				seq_descr = match.group(2)
				sequence = ''
		else:
			sequence += line
	fasta_dict[seqID] = {'sequence' : sequence, 'description' : seq_descr}
#print(fasta_dict)

for identifier in fasta_dict:
	nt_seq = fasta_dict[identifier]['sequence']
	countA = nt_seq.count('A')
	countC = nt_seq.count('C')
	countG = nt_seq.count('G')
	countT = nt_seq.count('T')
	fasta_dict[identifier]['nt_count'] = {'nt_count' : {'A' : countA, 'C' : countC, 'G' : countG, 'T' : countT}}
	print(identifier, fasta_dict[identifier]['nt_count'])
