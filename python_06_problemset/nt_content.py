#!/usr/bin/env python3

# for each seq calculate and store the count of each unique nt character in a dict
# report name, total nt count, and GC content of each seq

with open("Python_06.seq.txt", "r") as read_seq:
	for line in read_seq:
		line = line.rstrip()
		(seqID, seq) = line.split("\t")
		nt_count = {}
		for nt in set(seq):
			nt_count[nt] = seq.count(nt)
		print(seqID, nt_count, 'GC content: ', (nt_count['G'] + nt_count['C'])/len(seq))

