def to_rna(dna_strand):
    complement = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

    return ''.join(complement[nucleotide] for nucleotide in dna_strand)