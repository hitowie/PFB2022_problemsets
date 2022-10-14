#!/usr/bin/env python3

# generate gene lists

# open each of the alpaca gene files and add the geneIDs to a set (one set per file)

all_genes = "alpaca_all_genes.tsv"
stemcellproliferation = "alpaca_stemcellproliferation_genes.tsv"
pigmentation = "alpaca_pigmentation_genes.tsv"

gene_files = [all_genes, stemcellproliferation, pigmentation]

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
#print(geneID_dict[pigmentation])

# find all the genes that are not cell proliferation genes
print(f'all genes that are not cell proliferation genes: {geneID_dict[all_genes] - geneID_dict[stemcellproliferation]}')
# find all genes that are both stem cell proliferation genes and pigment genes
print(f'all genes that are both stem cell proliferation genes and pigment genes: {geneID_dict[all_genes] | (geneID_dict[stemcellproliferation] & geneID_dict[pigmentation])}')
