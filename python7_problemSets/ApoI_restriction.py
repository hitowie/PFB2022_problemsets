#!/usr/bin/env python3
import re

fasta_header = r"^>(\w+)\s?(.*)" 
ApoI_RS = r"[AG]AATT[CT]"

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
	match = re.findall(ApoI_RS, seq)
	print(match)

