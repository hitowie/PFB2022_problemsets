#!/usr/bin/env python3
import re

fasta_header = r"^>(\w+)\s?(.*)" 
ApoI_RS = r"[AG](AATT)[CT]"

fasta_file = open("Python_07_ApoI.fasta", "r")

# parse fasta file
seq_dict = {}
for line in fasta_file:
	line = line.rstrip()
	match = re.match(fasta_header, line)
	if match:
		seqID = match.group(1)
		seq_dict[seqID] = ''
	else:
		seq_dict[seqID] += line
fasta_file.close()

# find all ApoI restriction sites
for seqID in seq_dict:
	seq = seq_dict[seqID]
	RS = re.findall(ApoI_RS, seq)
	print(RS)
# determine the sites of the physical cuts by ApoI in the DNA sequence and print out the sequence with ^ at the cut sites
	new_seq = seq
	cut_sites = re.finditer(ApoI_RS, seq)
	for cut in cut_sites:
		pattern = "".join(cut.group(0))
		replacement = "".join([cut.group(1)[0], "^", cut.group(1)[1]])
		new_seq = re.sub(pattern, replacement, new_seq)
	print(new_seq)

# determine the lengths of your fragments and sort them by length (in the same order they would separate on electrophoresis gel)
	fragments = new_seq.split('^')
	electrophoresis = sorted(fragments, key=len, reverse=True)
	print(electrophoresis)
