# import gzip

# with gzip.open('GCF_016864115.1_ASM1686411v1_genomic.gbff.gz', mode="rt") as f:
#     file_content = f.read()
#     print(file_content)

# import gzip

# with gzip.open('GCF_016864115.1_ASM1686411v1_genomic.gbff.gz','rt') as f:
#     for line in f:
#         print('got line', line)

import gzip
import glob
import os
from Bio import GenBank

'''
    For the given path, get the List of all files in the directory tree 
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

def main() :      

	dirName = '/home/linuxipg/Damienrefseq/refseq/bacteria';

	# Get the list of all files in directory tree at given path
	listOfFiles = getListOfFiles(dirName)

	with open('file1.txt', 'w') as o:

			for elem in listOfFiles:
				if elem.endswith(".gbff.gz"):
					with gzip.open(elem, 'rt') as f:
						for line in f:
							#if 'country' in line:
							#	print(line, file=o, end='')
							# else:
							# 	print(line, "NA")
							#if 'PUBMED' in line:
							#	print(line, file=o, end='')
							# else:
							# 	print(line, "NA")
							#if 'host' in line:
							#	print(line, file=o, end='')
							# else:
							# 	print(line, "NA")
							if 'isolation_source' in line:
								print(line, file=o, end='')
							# else:
							# 	print(line, "NA")
							#if 'Genes' in line:
								#print(line, file=o, end='')
							# else:
							# 	print(line, "NA")
							#if 'LOCUS' in line:
								#print(line, file=o, end='')
							# else:
							# 	print(line, "NA")
				else:
					continue

					with open("file1.txt") as handle:

						for record in GenBank.parse(handle):

							print(record.accession)

if __name__ == '__main__':
    main()