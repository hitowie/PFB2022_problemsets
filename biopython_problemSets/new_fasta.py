#!/usr/bin/env python3
from Bio import SeqIO
import re

# Make a new fasta file of all the sequences containing the species 'Salmonella paratyphi B'. Call this protein file 's_paratyphi.prot.fa'. 
# You'll want to loop through all the sequence records, extract the description, find matches to 'Salmonella paratyphi B' and convert to fasta.

pattern = r"Salmonella paratyphi B"
 
with open('s_paratyphi.prot.fa', 'w') as new_fasta:
	for seq_record in SeqIO.parse('uniprot_sprot.fasta', 'fasta'):
		found = re.findall(pattern, str(seq_record.description))
		for f in found:
			new_fasta.write(f">{seq_record.description}\n{str(seq_record.seq)}\n")
