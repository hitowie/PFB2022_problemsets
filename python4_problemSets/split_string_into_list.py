#!/usr/bin/env python3

taxa = 'sapiens, erectus, neanderthalensis'

print(taxa)

# What's the first element of taxa?
print(taxa[1])

# What class is taxa?
print(type(taxa))

# split taxa into individual words and save the result in spceies 
print(taxa.split(', '))
species = taxa.split(', ')
print(species)

# What's the first element of species?
print(species[1])

# What class is species?
print(type(species))

# sort the list alphabetically
print(sorted(species))

# sort the list by length of each element
print(sorted(species, key=len))



