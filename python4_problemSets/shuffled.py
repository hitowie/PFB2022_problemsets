#!/usr/bin/env python3
import random

seq = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGG'
list = [nt for nt in seq]

#list=[]
#for i in string:
#	list.append(i)

N = len(seq)

for i in list:
	posA = random.randrange(N)
	A = list[posA]
	posB = random.randrange(N)
	B = list[posB]
	list[posA] = B
	list[posB] = A

print(''.join(list))
