# DNA Toolset/Code testing file

from DNAToolkit import *
import random

# Create a random DNA string 'randDNAstr to test the function validateSeq
randDNAseq = "".join([random.choice(Nucleotides)
                        for nuc in range(50)])


DNAstr = validateSeq(randDNAseq)
print(countNucFrequency(randDNAseq))