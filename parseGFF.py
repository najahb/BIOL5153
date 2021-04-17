#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO

# function to return the reverse complement of a feature
def rev_comp(feature):
    return feature.reverse_complement()

# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

# create an argument parser object
parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract each feature from the genome')

# add positional arguments
parser.add_argument('gff', help= 'name of the GFF file')
parser.add_argument('fasta', help = 'name of the FASTA file')

# parse the arguments
args = parser.parse_args()


# read in FASTA file
genome = SeqIO.read(args.fasta, 'fasta')
print(genome.id)
print(genome.seq)



# open and read in GFF file
with open(args.gff, 'r') as gff_in:

    #create a csv reader object
    reader = csv.reader(gff_in, delimiter='\t')

    # loop over all the lines in our reader object (i.e., parsed file)
    GENES = []
    CDS = []
    for line in reader:
        species = line[0].replace(' ','_')
        region = line[2]
        start  = line[3]
        end    = line[4]
        feature = genome.seq[int(start)-1:int(end)]
        strand = line[6]
        gene = line[8].split()[1]
        if region == 'CDS':
            if strand == '-':
                feature = rev_comp(feature)
            if gene not in GENES:
                GENES.append('%s_%s' % (species,gene))
                CDS.append('')
            CDS[-1] += str(feature)
            
        # extract the sequence of each feature from the genome
        print(">watermelon %s" % line[8])
        print(feature)
       

        # extract the sequence
        print(len(genome.seq))

        # print coding sequences for all genes
        print()
        for i in range(len(GENES)):
            print('>%s' % GENES[i])
            print(CDS[i])