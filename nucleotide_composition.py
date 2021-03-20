# set the name of input DNA sequence
filename = 'dna.txt'
# open filename
infile = open(filename,'r')
DNA_sequence = infile.read().rstrip()

# Sequence length
print('Sequence length: %d' % len(DNA_sequence))

# Freq of A
numA = DNA_sequence.count('A')
print('Freq of A: %.3F' % (numA/len(DNA_sequence)))

# Freq of C
numC = DNA_sequence.count('C')
print('Freq of C: %.3F' % (numC/len(DNA_sequence)))

# Freq of G
numG = DNA_sequence.count('G')
print('Freq of G: %.3F' % (numG/len(DNA_sequence)))

# Freq of T
numT = DNA_sequence.count('T')
print('Freq of T: %.3F' % (numT/len(DNA_sequence)))

# G+C content
print('G+C content: %.3f' % ((numG+numC)/len(DNA_sequence)))

# Simple check to make sure the frequencies sum to 1
print('Sum of Freqs: %.3f' % ((numC+numG+numT+numA)/len(DNA_sequence)))
