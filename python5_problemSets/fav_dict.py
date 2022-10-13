#!/usr/bin/env python3
import sys

# construct a dictionary of your favorite things
fav_dict = {
	'sport' : 'handball' ,
	'dessert' : 'ice cream' ,
	'person' : 'Franzi' ,
	'instrument' : 'drums'
	}

# add favorite organism to dict
fav_dict['organism'] = 'E.coli'

# change value of organism
fav_dict['organism'] = 'S.pombe'

print(f"Here are some favorite things to choose from:")
for k in fav_dict:
	print(k, end='\t')	# not happy with this output

# use an input variable as key
##fav_thing = input("\nChoose one category: ")

# taking two inputs to set a new value to the chosen key
x, y = input("\nChoose a category and name your favorite thing \n(type two words without using comma): ").split()
fav_thing = x
fav_dict[fav_thing] = y

# print favorite instrument
##print(f"My favorite instrument is {fav_dict['instrument']}")

# use `for` loop to print each key:value of dict
print("Here's the dictionary:\n")
for k in fav_dict:
	print(k,':\t', fav_dict[k])


print(f"\nMy favorite {fav_thing} is {fav_dict[fav_thing]}\n")

