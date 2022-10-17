#!/usr/bin/env python3
import sys
import re

# parse fasta
fasta_input = sys.argv[1]
#fasta_input = 'Python_07.fasta'

pattern = r"^>(\S+)\s+(.*)"
fasta_dict = {}
sequence = ''

with open(fasta_input, "r") as fasta_object:
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

# add nt composition to fasta_dict
for seq_record in fasta_dict:
	nt_comp = {}
	nt_seq = fasta_dict[seq_record]['sequence']
	unique_nt = set(nt_seq)
	for nt in unique_nt:
		count = nt_seq.count(nt)
		nt_comp[nt] = count
	fasta_dict[seq_record]['nt_composition'] = nt_comp
#	print(seq_record, fasta_dict[seq_record]['nt_composition'])
#print(fasta_dict)

# first reading frame
with open ("Python_08.codons-frame-1.nt", "w") as codons_frame1:
	for seq_record in fasta_dict:
		nt_seq = fasta_dict[seq_record]['sequence']
		split_seq = ''
		for codon in range(0, len(nt_seq), 3):
			split_seq += nt_seq[codon:codon+3] + ' '
#		print(f"{seq_record}-frame-1-codons\n{split_seq}\n")
		codons_frame1.write(f"{seq_record}-frame-1-codons\n{split_seq}\n")
print("written file 'Python_08.codons-frame-1.nt'")	

# adding all three reading frames to fasta_dict
with open ("Python_08.codons-3frames.nt", "w") as codons_frame3:
	for seq_record in fasta_dict:
		nt_seq = fasta_dict[seq_record]['sequence']
#		split_seq = ''
#		reading_frame = {}
		frame_start = [0, 1, 2]
		for start in frame_start:
			split_seq = ''
			for codon in range(start, len(nt_seq), 3):
				split_seq += nt_seq[codon:codon+3] + ' '
#			print(nt_seq.count('A'), '\t', split_seq.count('A'))
#			print(f"{seq_record}-frame-{start+1}-codons\n{split_seq}\n")
			codons_frame3.write(f"{seq_record}-frame-{start+1}-codons\n{split_seq}\n")
print("written file 'Python_08.codons-3frames.nt'")  

# adding all three reading frames plus three reading frames of the reverse complement
with open ("Python_08.codons-6frames.nt", "w") as codons_frame6:
	for seq_record in fasta_dict:
		nt_seq = fasta_dict[seq_record]['sequence']
		# built in reverse complement script from python3_problemSets
		seq_Gc = nt_seq.replace('G','c')
		seq_Cg_Gc = seq_Gc.replace('C','g')
		seq_At_Cg_Gc = seq_Cg_Gc.replace('A','t')
		seq_Ta_At_Cg_Gc = seq_At_Cg_Gc.replace('T','a')
		SEQ_complement = seq_Ta_At_Cg_Gc.upper()
		SEQ_reverse_complement = SEQ_complement[::-1]
		fasta_dict[seq_record]['reverse_complementary_sequence'] = SEQ_reverse_complement
#		print(seq_record,'\n', nt_seq, '\n', SEQ_reverse_complement)
		rev_seq = fasta_dict[seq_record]['reverse_complementary_sequence']
		reading_frame = {'rf_forward' : {}, 'rf_reverse' : {}}
		frame_start = [0, 1, 2]
		for start in frame_start:
			split_seq = ''
			rev_split_seq = ''
			frame = f'frame {start + 1}'
			aa_seq = ''
			for codon in range(start, len(nt_seq), 3):
				split_seq += nt_seq[codon:codon+3] + ' '
				rev_split_seq += rev_seq[codon:codon+3] + ' '
			reading_frame['rf_forward'][frame] = {'orf' : split_seq, 'translation' : aa_seq}
			reading_frame['rf_reverse'][frame] = {'orf' : rev_split_seq, 'translation' : aa_seq}
#			print('forward:', nt_seq.count('A'), '\t', split_seq.count('A'), '\t', 'reverse:', SEQ_reverse_complement.count('A'), '\t', rev_split_seq.count('A') )
			codons_frame6.write(f"{seq_record}-{frame}-forward-codons\n{split_seq}\n{seq_record}-{frame}-reverse-codons\n{rev_split_seq}\n")
		fasta_dict[seq_record]['reading_frame'] = reading_frame
#	print(fasta_dict)
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

with open("Python_08.translated.aa", "w") as peptide_file:
	for seq_record in fasta_dict:
		translation_list = []
		for frame in fasta_dict[seq_record]['reading_frame']['rf_forward']:
#			translation_list = []
			codons = re.findall(r"\w{3}", fasta_dict[seq_record]['reading_frame']['rf_forward'][frame]['orf'])
			for codon in codons:
				translation_list.append(translation_table[codon])
			aa_seq = ''.join(translation_list)
			translation_list = []
			fasta_dict[seq_record]['reading_frame']['rf_forward'][frame]['translation'] = aa_seq
#		print(fasta_dict[seq_record]['reading_frame']['rf_forward'][frame]['translation'])
			peptide_file.write(f"{seq_record}-{frame}-forward-strand\n{aa_seq}\n")
		for frame in fasta_dict[seq_record]['reading_frame']['rf_reverse']:
			codons = re.findall(r"\w{3}", fasta_dict[seq_record]['reading_frame']['rf_reverse'][frame]['orf'])
			for codon in codons:
				translation_list.append(translation_table[codon])			
			aa_seq = ''.join(translation_list)
			translation_list = []
			fasta_dict[seq_record]['reading_frame']['rf_reverse'][frame]['translation'] = aa_seq
#	print(fasta_dict[seq_record]['reading_frame'])
#		print(f"""{seq_record}-forward-strand-frame1-aa_seq\n
#{fasta_dict[seq_record]['reading_frame']['rf_forward'][frame]['translation']}\n
#""")
			peptide_file.write(f"{seq_record}-{frame}-reverse-strand\n{aa_seq}\n")
print("written file 'Python_08.translated.aa'")
#print(fasta_dict)

with open("Python_08.translated-longest.aa", "w") as orf_file:
	for seq_record in fasta_dict:
		longest_peptide = ''
		longest_length = 0
		for frame in fasta_dict[seq_record]['reading_frame']['rf_forward']:
			aa_string = fasta_dict[seq_record]['reading_frame']['rf_forward'][frame]['translation']
#			print(aa_string)
			find_peptide = re.findall(r"M\w+\*", aa_string)
			for peptide in find_peptide:
				if len(peptide) > longest_length:
					longest_length = len(peptide) 	# AttributeError: 'NoneType' object has no attribute 'group'
					longest_peptide = peptide
#				print("forward", frame, peptide)
		for frame in fasta_dict[seq_record]['reading_frame']['rf_reverse']:
			aa_string = fasta_dict[seq_record]['reading_frame']['rf_reverse'][frame]['translation']
#			print(aa_string)
			find_peptide = re.findall(r"M\w+\*", aa_string)
			for peptide in find_peptide:
				if len(peptide) > longest_length:
					longest_length = len(peptide) 	# AttributeError: 'NoneType' object has no attribute 'group'
					longest_peptide = peptide
#				print("reverse", frame, peptide)
#		print(longest_peptide)
#		print(f"{seq_record}\n{longest_peptide}")
		orf_file.write(f"{seq_record}\n{longest_peptide}\n")
print("written file 'Python_08.translated-longest.aa'")
