#!/usr/bin/env python3
import sys
import re

# parse fasta
fasta_input = sys.argv[1]
#fasta_input = 'Python_07.fasta'

pattern = r"^>(\S+)\s+(.*)"
fasta_dict = {}
sequence = ''

with open(fasta_input, "r") as fasta_object:
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

# add nt composition to fasta_dict
for seq_record in fasta_dict:
	nt_comp = {}
	for nt_seq in fasta_dict[seq_record]['sequence']:
		unique_nt = set(nt_seq)
		for nt in unique_nt:
			count = nt_seq.count(nt)
			nt_comp[nt] = count
	fasta_dict[seq_record]['nt_composition'] = nt_comp
	print(seq_record, fasta_dict[seq_record]['nt_composition'])
#print(fasta_dict)
