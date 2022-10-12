#!/usr/bin/env python3

seq_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for seq in seq_list:
	print(f"{seq_list.index(seq)} \t {len(seq)} \t {seq}") 

