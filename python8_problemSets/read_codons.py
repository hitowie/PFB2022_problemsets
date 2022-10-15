#!/usr/bin/env python3
import sys
import re

# take a multi FASTA file from user input and break each sequence into codons in just one reading frame

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

with open("Python_08.codons-frame-1.nt", "w") as write_file:
	for identifier in fasta_dict:
		nt_seq = fasta_dict[identifier]['sequence']
		split_seq = ''
		for i in range(0, len(nt_seq), 3):
			split_seq += nt_seq[i:i+3] + ' '
		write_file.write(f"{identifier}-frame-1-codons\n{split_seq}\n")
print("written file 'Python_08.codons-frame-1.nt'")

# break each sequence into codons in all three reading frames
with open("Python_08.codons-3frames.nt", "w") as write_file2:
	for identifier in fasta_dict:
		nt_seq = fasta_dict[identifier]['sequence']
		frame1 = ''
		frame2 = ''
		frame3 = ''
		for i in range(0, len(nt_seq), 3):
			frame1 += nt_seq[i:i+3] + ' '
		for i in range(1, len(nt_seq), 3):
			frame2 += nt_seq[i:i+3] + ' '
		for i in range(2, len(nt_seq), 3):
			frame3 += nt_seq[i:i+3] + ' '
		write_file2.write(f"""{identifier}-frame-1-codons\n{frame1}\n
{identifier}-frame-2-codons\n{frame2}\n
{identifier}-frame-3-codons\n{frame3}\n""")
print("written file 'Python_08.codons-3frames.nt'")

# reverse complement each sequence and print out all six reading frames
with open("Python_08.codons-6frames.nt", "w") as write_file3:
	for identifier in fasta_dict:
		nt_seq = fasta_dict[identifier]['sequence']
		# use reverse complement script from python3_problemSets
		seq_Gc = nt_seq.replace('G','c')
		seq_Cg_Gc = seq_Gc.replace('C','g')
		seq_At_Cg_Gc = seq_Cg_Gc.replace('A','t')
		seq_Ta_At_Cg_Gc = seq_At_Cg_Gc.replace('T','a')
		SEQ_complement = seq_Ta_At_Cg_Gc.upper()
		SEQ_reverse_complement = SEQ_complement[::-1]
		frame1 = ''
		frame2 = ''
		frame3 = ''
		frame4 = ''
		frame5 = ''
		frame6 = ''
		for i in range(0, len(nt_seq), 3):
			frame1 += nt_seq[i:i+3] + ' '
		for i in range(1, len(nt_seq), 3):
			frame2 += nt_seq[i:i+3] + ' '
		for i in range(2, len(nt_seq), 3):
			frame3 += nt_seq[i:i+3] + ' '
		for i in range(0, len(SEQ_reverse_complement), 3):
			frame4 += nt_seq[i:i+3] + ' '
		for i in range(1, len(SEQ_reverse_complement), 3):
			frame5 += nt_seq[i:i+3] + ' '
		for i in range(2, len(SEQ_reverse_complement), 3):
			frame6 += nt_seq[i:i+3] + ' '
		write_file3.write(f"""{identifier}-frame-1-codons\n{frame1}\n
{identifier}-frame-2-codons\n{frame2}\n
{identifier}-frame-3-codons\n{frame3}\n
{identifier}-frame-4-codons\n{frame4}\n
{identifier}-frame-5-codons\n{frame5}\n
{identifier}-frame-6-codons\n{frame6}\n""")
print("written file 'Python_08.codons-6frames.nt'")



