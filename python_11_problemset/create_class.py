#!/usr/bin/env python3

# create a DNA sequence class that will contain a sequence, its name, and its organism of origin

class DNARecord(object):

	def __init__(self, sequence, seq_name, organism):
		self.sequence = sequence
		self.seq_name = seq_name
		self.organism = organism

# sequence length method
	def length(self):
		return len(self.sequence)

# nucleotide composition method
	def nt_composition(self):
		unique_nt = set(self.sequence)
		nt_count = {}
		for nt in unique_nt:
			count = self.sequence.count(nt)
			nt_count[nt] = count
		return nt_count

# GC content method
	def gc_content(self):
		gc_content = (self.sequence.count('G') + self.sequence.count('C'))/len(self.sequence)
		return gc_content

# FASTA formatter method
	def fasta_format(self):
		print(f">{self.seq_name} {self.organism}\n{self.sequence}")

# compare two DNA Sequence records method
	def compare_to(self, other):
		print(f"{self.seq_name} {self.organism} {self.sequence}" == f"{other.seq_name} {other.organism} {other.sequence}")
		

# write some lines of code outside your class that
# a. uses the object sequence attribute to retrieve and print the sequence
# b. uses the object name attribute to retrieve and print the name
# c. uses the object organism attribute to retrieve and print the organism
# d. uses the new methods

dna_rec_obj = DNARecord('ACTGATCGTTACGTACGAGT', 'ABC1', 'Drosophila melanogaster')
print(dna_rec_obj.sequence)
print(dna_rec_obj.seq_name)
print(dna_rec_obj.organism)
print(dna_rec_obj.length())
print(dna_rec_obj.nt_composition())
print(dna_rec_obj.gc_content())
dna_rec_obj.fasta_format()

dna_rec_obj2 = DNARecord('ACTGATCGTTACGTACGAGT', 'ABC1', 'Drosophila melanogaster')
dna_rec_obj3 = DNARecord('ACTGATCGTTACGTACGAGT', 'ABCD', 'Drosophila melanogaster')

print(dna_rec_obj.compare_to(dna_rec_obj2))
print(dna_rec_obj.compare_to(dna_rec_obj3))
