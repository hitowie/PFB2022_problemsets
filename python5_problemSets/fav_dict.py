#!/usr/bin/env python3
import sys

# construct a dictionary of your favorite things
fav_dict = {
	'sports' : 'handball' ,
	'dessert' : 'ice cream' ,
	'person' : 'Franzi' ,
	'instrument' : 'drums'
	}

print(f"Here are some favorite things to choose from:")
for k in fav_dict:
	print(k, end='\t')

# use an input variable as key
##fav_thing = input("\nChoose one category: ")

# taking two inputs to set a new value to the chosen key
x, y = input("\nChoose a category and name your favorite thing (type two words  without using comma): ").split()
fav_thing = x
fav_dict[fav_thing] = y

# print favorite instrument
##print(f"My favorite instrument is {fav_dict['instrument']}")

# add favorite organism to dict
fav_dict['organism'] = 'E.coli'

# change value of organism
fav_dict['organism'] = 'S.pombe'



print(f"My favorite {fav_thing} is {fav_dict[fav_thing]}")

