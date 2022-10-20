#!/usr/bin/env python3
from Bio import SeqIO
import re

# generate a list of all the IDs in the fasta file
# make a list of all the descriptions, using regular expressions, extract just the genus and species and count the number of sequences present for that genus/species combination

record_ids = []
#descriptions = []
regex = r"OS=(.+)OX="
genus_species_list = []
genus_species = ''
genus_species_dict = {}

for seq_record in SeqIO.parse('uniprot_sprot.fasta', 'fasta'):
	record_ids.append(seq_record.id)
#	descriptions.append(seq_record.description)
	matches = re.finditer(regex, seq_record.description)
	for match in matches:
		genus_species_list.append(match.group(1))

unique_genus_species_list = set(genus_species_list)
for genus_species in unique_genus_species_list:
	count_genus_species = genus_species_list.count(genus_species)
	if genus_species not in genus_species_dict:
		genus_species_dict[genus_species] = count_genus_species
#	genus_species_dict[genus_species] = [genus_species_list.count(genus_species) for genus_species in unique_genus_species_list if genus_species not in genus_species_dict] ### need to do dictionary comprehension here!

print(record_ids)
#print(descriptions)
#print(genus_species_list)
#print(unique_genus_species_list)
print(genus_species_dict)

# Make a new fasta file of all the sequences containing the species 'Salmonella paratyphi B'. Call this protein file 's_paratyphi.prot.fa'. 
# You'll want to loop through all the sequence records, extract the description, find matches to 'Salmonella paratyphi B' and convert to fasta.

#pattern = r"Salmonella\sparathyphi\sB"

#with open('s_paratyphi.prot.fa', 'w') as new_fasta:
#	for seq_record in SeqIO.parse('uniprot_sprot.fasta', 'fasta'):
#		found = re.finditer(pattern, seq_record.description)
#		for f in found:
#			new_fasta.write(f">{seq_record.description}\n{seq_record.seq}")
			
