#!/usr/bin/env python3
import sys
from Bio import SeqIO

fasta_file = sys.argv[1]

# Create a new FASTA parser that uses BioPython to get the sequence name, description, and sequence
# Add in some code to print out stats about your FASTA records in your mult-FASTA file
sequence_count = 0
total_num_nts = 0
shortest_sequence = ''
shortest_len = 999999999999
longest_sequence = ''
longest_len = 0
avg_GC_content = 0
sequence_highest_GC = ''
highest_GC_content = 0
sequence_lowest_GC = ''
lowest_GC_content = 100
total_GC_content = 0
total_num_GC = 0

for seq_record in SeqIO.parse(fasta_file, "fasta"):
	print(f"{seq_record.id}\t{seq_record.description}\n{seq_record.seq}")
	sequence_count +=1
	total_num_nts += len(seq_record.seq)
	if len(seq_record.seq) > longest_len:
		longest_len = len(seq_record.seq)
		longest_sequence = seq_record.id
	if len(seq_record.seq) < shortest_len:
		shortest_len = len(seq_record.seq)
		shortest_sequence = seq_record.id
	GC_content = seq_record.seq.count('G' or 'C' or 'g' or 'c') / len(seq_record.seq)
#	print(GC_content)
	total_GC_content += GC_content
	total_num_GC += seq_record.seq.count('G' or 'C' or 'g' or 'c')
	if GC_content > highest_GC_content:
		highest_GC_content = GC_content
		sequence_highest_GC = seq_record.id
	if GC_content < lowest_GC_content:
		lowest_GC_content = GC_content
		sequence_lowest_GC = seq_record.id
avg_len = total_num_nts / sequence_count
avg_GC_content = total_GC_content / sequence_count
avg_GC = total_num_GC / total_num_nts
print("\n")
print(f"sequence count: {sequence_count}")
print(f"total number of nucleotides: {total_num_nts}")
print(f"avg len: {avg_len}")
print(f"shortest len: {shortest_sequence} {shortest_len}")
print(f"longest len: {longest_sequence} {longest_len}")
print(f"avg GC content: {avg_GC_content} or {avg_GC}")
print(f"highest GC content: {sequence_highest_GC} {highest_GC_content}")
print(f"lowest GC content: {sequence_lowest_GC} {lowest_GC_content}")
