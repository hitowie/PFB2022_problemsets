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
# if the enzyme is present in enzyme_dict AND can cut the sequence, print out:
# sequence, annotated with cut sites
# number of fragments
# fragment sorted largest to smallest

