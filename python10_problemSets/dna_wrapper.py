#!/usr/bin/env python3
import sys
import re

# create a function to format a string of DNA so that each line is no more than 60nt long
# modify your function so that it will work whether the DNA string does or does not have new lines
# modify your function so that it takes two arguments, the DNA string and the max length of each line
# modify your script so that it can take two command line arguments

fasta_file = open(sys.argv[1], 'r')
width = sys.argv[2]

def wrap_dna(dna, width):
	dna = re.sub(r"\n", "", dna)
	regex = re.compile(r"\w{" + str(width) + "}")
	lines = regex.findall(dna)
	for line in lines:
		print(line)

fasta_dict = {}
for line in fasta_file:
	line = line.rstrip()
	match = re.match(r'>(|S+)', line)
	if line.startswith('>'):
		seqID = line
		fasta_dict[seqID] = ''
	else:
		fasta_dict[seqID] += line

for record in fasta_dict:
	print(record)
	wrap_dna(dna = fasta_dict[record], width = width)



dna1 = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'

#wrap_dna(dna1)


dna2 = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''

#wrap_dna(dna2)

#wrap_dna(dna2, 40)