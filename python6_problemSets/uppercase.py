#!/usr/bin/env python3

# open and read content of Python_06.txt
# uppercase each line and print to STDOUT
##with open("Python_06.txt", "r") as file_read:
##	for line in file_read:
##		line = line.rstrip()
##		print(line.upper())

# write result to new file Python_06_uc.txt
with open("Python_06.txt", "r") as file_read, open("Python_06_uc.txt", "w") as file_write:
	for line in file_read:
		line = line.rstrip()
		file_write.write(line.upper() + "\n")
print("wrote 'Python_06_uc.txt'")
