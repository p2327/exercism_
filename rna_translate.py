from collections import deque

def rna_translate(seq):
"""A rna translation machine using a dispatch dictionary and deque"""
    
    bases = list(seq) # prepare list of ribonucleic bases
    bases_q = deque(aminos)
    codon = []
    protein = []
    
    def ribosome(s):
        if len(bases_q) == 0:
            return protein
        while len(codon) <= 3:
            codon.append(bases_q.popleft())
            if len(codon) == 3:
                snip = ''.join(codon[0:3]) # assembly the codon
                return translate(snip) 
                
    def translate(c): # reads the codon snip into an amino acid
        nonlocal protein
        nonlocal codon
        stop_codons = ['UAA', 'UAG', 'UGA']
        if c in stop_codons:
            return protein
        protein += [dispatch[c]]
        codon = [] # reset the codon
        return ribosome(codon)
        
    dispatch = {'AUG':'Methyonine',
                'UUU':'Phenylalanine',
                'UUC':'Phenylalanine',
                'UUG':'Leucine',
                'UUA':'Leucine',
                'UAU':'Tyrosine',
                'UAC':'Tyrosine',
                'UGU':'Cysteine',
                'UGC':'Cysteine',
                'UGG':'Tryptophan,
                'UAA':'STOP',
                'UAG':'STOP',
                'UGA':'STOP'
                }
                
    return ribosome(bases_q)
