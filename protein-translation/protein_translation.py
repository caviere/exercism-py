def proteins(strand):
    codons = {'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan'}

    proteins = []
    while len(strand) > 0:
        if strand [:3] in ('UAA', 'UAG', 'UGA'):
            break
        proteins.append(codons[strand[0:3]])
        strand = strand[3:]
    return proteins
