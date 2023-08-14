#!/usr/bin/env python3
import random

# create a shuffled sequence
# use a `for` loop to switch two random nucleotides N times with N=len(seq)

seq = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGG'

N = len(seq)

for i in list(seq):
	posA = random.randrange(N)
	A = list(seq)[posA]
	posB = random.randrange(N)
	B = list(seq)[posB]
	list(seq)[posA] = B
	list(seq)[posB] = A

print(''.join(list(seq)))

