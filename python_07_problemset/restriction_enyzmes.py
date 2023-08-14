#!/usr/bin/env python3
import re
import sys

# fill a dictionary of enyzmes paired with their recognition patterns

with open("rebase.txt","r") as enzyme_file:
	enzyme_dict = {}
	lines_after_header = enzyme_file.readlines()[10:]	# skip the top 10 header lines of the file
	pattern = r"^(\S+\s\S*)\W+(\S+)"
	for line in lines_after_header:
		line = line.rstrip()
		matches = re.finditer(pattern, line) # re.search().group() does not work, use finditer() and for loop to call match.group()
		for match in matches:
			enzyme = match.group(1)
			recognition_site = match.group(2)
			enzyme_dict[enzyme] = recognition_site
print(enzyme_dict)

# take two command line arguments: enzyme and fasta file with sequence to be cut
user_enzyme = sys.argv[1]

# parse in fasta file
pattern = r"^>(\w+)\s?(.*)"
fasta_dict = {}

with open(sys.argv[2], "r") as fasta_file:
	for line in fasta_file:
		line = line.rstrip()
		if line.startswith(">"):
			header = line
			fasta_dict[header] = ''
		else:
			fasta_dict[header] += line

# search in enzyme_dict for restriction enzyme and restriction site
for enzymes in enzyme_dict:
	cut_site = enzyme_dict[enzymes]
# check if the enzyme is present in enzyme_dict
	if user_enzyme in enzymes:
#		print('enzyme found:', enzymes, 'cuts at', cut_site )	
#	check if user_enzyme can cut the sequence
		pattern_to_search_for = cut_site.replace('^','')
		replacement = cut_site 
		for seqID in fasta_dict:
			seq = fasta_dict[seqID]
			matches = re.finditer(pattern_to_search_for, seq)
			for match in matches:
				if match:
					new_seq = re.sub(pattern_to_search_for, replacement, seq)
			fragments = new_seq.split("^")
			electrophoresis = sorted(fragments, key=len, reverse=True)
			print(f"sequence with annotated cut sites: {new_seq}")
			print(f"number of fragments: {len(fragments)}")
			print(f"fragments sorted largest to smallest: {electrophoresis}")

