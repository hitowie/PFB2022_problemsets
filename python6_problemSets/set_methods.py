#!/usr/bin/env python3

# create a set using two different syntaxes
mySet1 = set('ATGTGGG')
mySet2 = {'ATGCCT'}
mySet3 = {'A','T','G','T','G','G','G'}

# are the two sets the same? does it matter how you create the set?
print(f'Set1: {mySet1}')
print(f'Set2: {mySet2}')
print(f'Set1 and Set2 are the same \t <= \t {mySet1 == mySet2}')
print(f'\nSet1: {mySet1}')
print(f'Set3: {mySet3}')
print(f'Set1 and Set3 are the same \t <= \t {mySet1 == mySet3}')

# find the intersection, difference, union, and symmetrical difference between Set A and B
setA = {3, 14, 15, 9, 26, 5, 35, 9}
setB = {60, 22, 14, 0, 9}

print(f'\nSetA: {setA}')
print(f'SetB: {setB}\n')

print(f'intersection: {setA & setB}')
print(f'difference: {setA - setB}')
print(f'union: {setA | setB}')
print(f'symmetrical difference: {setA ^ setB}')

