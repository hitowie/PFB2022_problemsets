#!/usr/bin/env python3

# calculate sequence identity
# aligned two similar dna sequences with ClustalW (result in FASTA format))
# stored alignment result in dna1 and dna2 (remove line breaks)

dna1 = 'AGCAC----CCTCCCACCTCATCCCACCCTTCTGATCTCAATCCAACG-TCG-----------CATCTCCACCGTCTCGC-GGATCGACCCAG----CGAAGTCCCTC--CCGCC--CCCAAAGTCCC--------CCAAATCTTGCAGT-TCCCTCCTAAATCCTCCCCA----TATAAACC-------AA---CCCCC-CGCCCTCAGATCCCTAATCCCA--------TCGCAAGC-ATCAGACTCCCTC---C-AAAGCAG---GCA--------------GCAGCTCCTC-TTCTTCCTAATCACACTATCTCGGAGAG-------------------------GAGCGGCCATGTCTGGGCGCGACAAGGGCGGCAAGGGGCTGGGCAAGGGCGGCGCCAAGCGGCACCGGAAGGTCCTCCGCGACAACATCCAGGGCATCACCAAGCCGGCGATCCGGAGGCTGGCCAGGAGGGGCGGCGTGAAGCGCATCTCCGGCCTCATCTACGAGGAGACCCGCGGCGTCCTCAAGATCTTCCTCGAGAACGTCATCCGCGACGCCGTCACCTACACCGAGCACGCCCGCCGCAAAACCGTCACCGCCATGGACGTCGTCTACGCGCTCAAGCGCCAGGGCCGCACCCTCTACGGCTTCGGAGGCTAGA---TTTGT--------GTGGTGAAGCAA----CTTCCTCGT---TTGCTCTGTGATCTGTGC---TGTCGTAGATGAGATTTAC-TGATTT--------------GGCGTGCGCCGGTTGTATTCTGTCATGGGGTTCA-----GTGGGCTGTGTAATACCTTGCTCTGTACTTCTGTTCAATGCAATCACTT-CTATTCTGAA'

dna2 = 'TCTAGAGATGGCGCCATTTGATTCCAGCAGCCACAAAGCACTAGAACAATCGATGCTAAGAGGTGACAGGAAAAACAGGCTGCAAAGACCCAGACAATGGAATGCAGCGGTGGTCAGCCTAAAACACTGTAGAAGGGCAAGATGAGCTGAGTAATTTTTAACTGGGCATCATTTTTAGAAACTGGAGTTTAAGTACCCCCTTTTCCATTTTTTCCTGAAGTCGTGGGCAGGGCGCAAGGTCTGTGAATCGGCCGACCGGATGCAGCTGGTGTGGAGAGTTCCCAATCAGGTCCGATTTATTACTATATAAAGTACTGCTGCGAGGCTTGCCGTGTTGCATTTTGTTTAGTACAAGACATGTCTGGGCGCGGCAAAGGCGGGAAGGGTCTGGGCAAAGGAGGCGCTAAGCGCCACCGCAAAGTTCTGCGCGACAACATTCAGGGCATCACCAAGCCCGCCATCCGACGCCTGGCACGGCGTGGAGGCGTTAAGCGCATCTCAGGCCTTATATACGAGGAGACACGCGGAGTTCTTAAAGTGTTTTTGGAGAATGTAATCCGCGATGCAGTTACCTACACGGAGCACGCCAAACGCAAGACAGTCACAGCCATGGACGTGGTTTACGCGCTCAAGCGCCAGGGCCGCACCCTGTATGGCTTTGGCGGCTGAGTGTTTTACTTACTTACACGGTTCCTCAAAGGCCCTTCTCAGGGCCACCCATGAAGTCTGTGAAAGAGCTGTAGACTAAAGATAGTTAATTTCTTAAGAACACTTAAACGTATGGCAGTTTTGGCAAATTAGCGATTCCACATAAGCAGTCGCTGAAGTTTGAGGTTCGGTGCCCCT-TTCA--GC-ATTACTTAGTGGTTAAAA'

count = 0

# compare each index for nucleotide differences
for nt in list(range(len(dna1))):
	if dna1[nt] == dna2[nt]:
		count += 1

print(f'Percent identity: {count/len(dna1)}')	

# python result: 0.5354691075514875	
# TCoffee result: 64.73%

