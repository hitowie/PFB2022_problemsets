#!/usr/bin/env python3
import sys

# Write a python script to trim poor-quality bases from the ends of the FASTQ sequences and output a new FASTQ file

fastq_file_name = sys.argv[1]
minimum_base_quality_threshold = int(sys.argv[2])

header = ''
sequence_string = ''
quality_string = ''
slice_index = 0
sliced_sequence = ''
sliced_quality = ''

with open(fastq_file_name, 'r') as fastq_obj, open(f'trimmed_{fastq_file_name}', 'w') as trimmed_obj:
#with open('test.fastq', 'r') as fastq_obj, open('trimmed_test.fastq', 'w') as trimmed_obj:
	line_counter = 0
	for line in fastq_obj:
		line = line.rstrip()
		line_counter += 1
		if line_counter % 4 == 1:
			header = line
			trimmed_obj.write(f"{header}\n")
		if line_counter % 4 == 2:
			sequence_string = line
		if line_counter % 4 == 0:
			quality_string = line
# iterate from the 3'-end of the read to the 5'-end, examining the quality values at each base position
			for index, ascii_char in enumerate(quality_string[::-1]):
# convert quality string characters to numeric values
				phred_score = ord(ascii_char) - 64
#       print(phred_score, end=' ') 
# break at the first base with a quality value greater-than or equal-to your inputted quality threshold
				if phred_score >= minimum_base_quality_threshold:
					slice_index_right = index
#         print(slice_index_right)
					break
			for index, ascii_char in enumerate(quality_string[:]):
				phred_score = ord(ascii_char) - 64
				if phred_score >= minimum_base_quality_threshold:
					slice_index_left = index
					break
# then use string slicing to extract the high-quality portion of both the sequence and quality strings
			sliced_sequence = sequence_string[slice_index_left:-1-slice_index_right]
			sliced_quality = quality_string[slice_index_left:-1-slice_index_right]
			trimmed_obj.write(f"{sliced_sequence}\n+\n{sliced_quality}\n")
#   print(f"{header}\n{sliced_sequence}\n+\n{sliced_quality}") 

