#!/usr/bin/env python3

# open the transcription factor file and the cell proliferation gene list file
# add the geneIDs to a set (one set per file)

transcriptionfactor = "alpaca_transcriptionFactors.tsv"
stemcellproliferation = "alpaca_stemcellproliferation_genes.tsv"

gene_files = [stemcellproliferation, transcriptionfactor]

geneID_dict = {}

for file in gene_files:
	with open(file, "r") as raw:
		geneID_list = []
		for line in raw:
			if line.startswith("E"):
				list_line = line.rstrip().split()
				geneID = list_line[0]
				geneID_list.append(geneID)
			geneID_set = set(geneID_list)
			geneID_dict[file] = geneID_set

# find all the genes that are transcription factors for stem cell proliferation
print(f'all genes that are transcription factors for stem cell proliferation genes: {geneID_dict[transcriptionfactor] & geneID_dict[stemcellproliferation]}')

