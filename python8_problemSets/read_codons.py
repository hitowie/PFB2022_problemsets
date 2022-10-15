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

# translate each of the six reading frames into amino acids
translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
		'TGG':'W',
		'TAT':'Y', 'TAC':'Y',
		'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}


with open("Python_08.translated.aa", "w") as write_file4:
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
		translation1 = []
		translation2 = []
		translation3 = []
		translation4 = []
		translation5 = []
		translation6 = []
		for i in range(0, len(nt_seq), 3):
			frame1 += nt_seq[i:i+3] + ' '
		codons1 = re.findall(r"\w{3}",frame1)
		for codon1 in codons1:
			translation1.append(translation_table.get(codon1))
		aa_seq1 = ''.join(translation1)
		for i in range(1, len(nt_seq), 3):
			frame2 += nt_seq[i:i+3] + ' '
		codons2 = re.findall(r"\w{3}",frame2)
		for codon2 in codons2:
			translation2.append(translation_table.get(codon2))
		aa_seq2 = ''.join(translation2)
		for i in range(2, len(nt_seq), 3):
			frame3 += nt_seq[i:i+3] + ' '
		codons3 = re.findall(r"\w{3}",frame3)	
		for codon3 in codons3:
			translation3.append(translation_table.get(codon3))
		aa_seq3 = ''.join(translation3)
		for i in range(0, len(SEQ_reverse_complement), 3):
			frame4 += nt_seq[i:i+3] + ' '
		codons4 = re.findall(r"\w{3}",frame4)
		for codon4 in codons4:
			translation4.append(translation_table.get(codon4))
		aa_seq4 = ''.join(translation4)
		for i in range(1, len(SEQ_reverse_complement), 3):
			frame5 += nt_seq[i:i+3] + ' '
		codons5 = re.findall(r"\w{3}",frame5)
		for codon5 in codons5:
			translation5.append(translation_table.get(codon5))
		aa_seq5 = ''.join(translation5)
		for i in range(2, len(SEQ_reverse_complement), 3):
			frame6 += nt_seq[i:i+3] + ' '
		codons6 = re.findall(r"\w{3}",frame5)
		for codon6 in codons6:
			translation6.append(translation_table.get(codon6))
		aa_seq6 = ''.join(translation6)
		write_file4.write(f"""{identifier}-frame-1-aa\n{aa_seq1}\n
{identifier}-frame-2-aa\n{aa_seq2}\n
{identifier}-frame-3-aa\n{aa_seq3}\n
{identifier}-frame-4-aa\n{aa_seq4}\n
{identifier}-frame-5-aa\n{aa_seq5}\n
{identifier}-frame-6-aa\n{aa_seq6}\n""")
print("written file 'Python_08.translated.aa'")

# find the longest peptide sequence (M=>*) of all six translated reading frames for a single sequence in all sequence records
# print 'Python_08.codons-6frames.nt' in FASTA format
with open("Python_08.translated-longest.aa", "w") as write_file5:
	for identifier in fasta_dict:	
		find_peptide1 = re.search(r"M\w+\*", aa_seq1)	
		peptide1 = find_peptide1.group(0)
		find_peptide2 = re.search(r"M\w+\*", aa_seq2)
		peptide2 = find_peptide2.group(0)
		find_peptide3 = re.search(r"M\w+\*", aa_seq3)
		if find_peptide3: # no peptide3 found
			peptide3 = find_peptide3.group(0)
		else:
			peptide3 = ''
		find_peptide4 = re.search(r"M\w+\*", aa_seq4)
		peptide4 = find_peptide4.group(0)
		find_peptide5 = re.search(r"M\w+\*", aa_seq5)
		peptide5 = find_peptide5.group(0)
		find_peptide6 = re.search(r"M\w+\*", aa_seq6)
		peptide6 = find_peptide6.group(0)
# print(find_peptide3)
	write_file5.write(f"""{identifier}-frame1-peptide\n{peptide1}\n
{identifier}-frame2-peptide\n{peptide1}\n
{identifier}-frame-3-peptide\n{peptide3}\n
{identifier}-frame-4-peptide\n{peptide4}\n
{identifier}-frame-5-peptide\n{peptide5}\n
{identifier}-frame-6-peptide\n{peptide6}\n""")
print("written file 'Python_08.translated-longest.aa'")
