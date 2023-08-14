#!/usr/bin/env python3

# Blast a protein such as purH against the S. paratyphi B proteins
# Print the E-value and the score and the length of the alignment and the % similiarity (not % identity)

# First format you FASTA file so that BLAST+ can use it as a database
# % makeblastdb -in s_paratyphi.prot.fa -dbtype prot -parse_seqids -out s_paratyphi.prot.db.fa

# Run blastp and create output in XML format
# % blastp -query purH.aa.fa -db s_paratyphi.prot.db.fa -out purH_blast_Sparatyphi.xml -evalue 1e-5 -outfmt 5

# Use BioPython to parse your XML BLAST results. Print out all the hit sequence ID that are better than 1e-5 as well as their descriptions in tab separated columns

from Bio.Blast import NCBIXML
result_handle = open("purH_blast_SparatyphiB.xml")
blast_records = NCBIXML.parse(result_handle)
for blast_record in blast_records:
	for alignment in blast_record.alignments:
		for hsp in alignment.hsps:
			if hsp.expect < 1e-5:
				print(f'hit_id: {alignment.title} E: {hsp.expect}', sep="\t")

