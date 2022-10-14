#!/usr/bin/env python3

# open and print the reverse complement of each sequence in Python_06.seq.txt
# print output in fasta format

with open("Python_06.seq.txt", "r") as seq_read:
	for line in seq_read:
		line = line.rstrip()
		(seqName, seq) = line.split("\t")
		# use reverse_complement script from python3_problemSets:
		seq_Gc = seq.replace('G','c')
		seq_Cg_Gc = seq_Gc.replace('C','g')
		seq_At_Cg_Gc = seq_Cg_Gc.replace('A','t')
		seq_Ta_At_Cg_Gc = seq_At_Cg_Gc.replace('T','a')
		SEQ_complement = seq_Ta_At_Cg_Gc.upper()
		SEQ_reverse_complement = SEQ_complement[::-1]
		print(f">{seqName} reverse complement \n{SEQ_reverse_complement}")

# in the command line direct STDOUT into new file
# ./reverse_complement.py > Python_06_seq_reverse_complement.fasta

