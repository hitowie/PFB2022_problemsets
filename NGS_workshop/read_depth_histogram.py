#!/usr/bin/env python3
import math
# compute a text histogram of genomic read depth
# use a dict with depth as the key and the count of bases as the value

read_depth_dict = {}
read_depth_list = []

with open('SRR21901339.read_depth.out', 'r') as fh:
	for line in fh:
		line = line.rstrip()
		chromosome, pos, depth = line.split("\t")
#	print(type(depth))
		read_depth_list.append(int(depth))
#	print(read_depth_list)
	
unique_read_depth = set(read_depth_list)
for d in unique_read_depth:
	base_count = read_depth_list.count(d)				
	read_depth_dict[d] = base_count
#print(read_depth_dict)
# sort dictionary by keys
#print(dict(sorted(read_depth_dict.items())))
x_list = []
count_list = []
with open("SRR21901339.read_depth.hist", "w") as histogram:
	for key in dict(sorted(read_depth_dict.items())):
		histogram.write(f'{key} | {"]" * read_depth_dict[key]}\n')
#	print("]" * read_depth_dict[key])
		x = read_depth_dict[key] * key
		x_list.append(x)
		count_list.append(read_depth_dict[key])
mean_depth = sum(x_list) / sum(count_list)
#print(sum(x_list))
#print(sum(count_list))
print(f"mean depth: {mean_depth}")
y_list = []
for key in read_depth_dict:
	y = (key - mean_depth)**2
	y_list.append(y)
#print(y_list)
stdev = math.sqrt(sum(y_list) / sum(count_list))
print(f"stdev: {stdev}") 
