# A module for Bio prog exercises pg 110
# But first validate the seq
def validate(seq):
    """Checks if the DNA seq has valid letters i.e A,T,C,G """
    val = ['A', 'T', 'C', 'G']
    seq = seq.upper()
    for letter in seq:
        if letter not in val:
            return "Invalid"
    return "Valid"


def dna_read(seq):
    """Reads a DNA seq,converts it to capital letters & counts purines & pyrimidines"""
    seq = seq.upper()
    purines = seq.count('A') + seq.count('G')
    pyrimidines = seq.count('C') + seq.count('T')
    return "Purines:" + str(purines) + " Pyrimidines:" + str(pyrimidines)


def rev_check(seq):
    """Reads a DNA seq & checks if it is equal to its reverse complement"""
    seq = seq.upper()
    nu_bind = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    comp = ''
    for nucleotide in seq:
        comp += nu_bind[nucleotide]
    return seq == comp[::-1]


def cg_count(seq):
    """Returns the total number of CG duplets contained in seq"""
    seq = seq.upper()
    return seq.count('CG')


def first_pro(seq):
    """Returns the size of  1st protein 2 be encoded (in any 3 reading frames) & returns -1 if no protein found"""
    """Translates a codon into an aminoacid using an internal
    dictionary with the standard genetic code."""
    seq = seq.upper()
    tc = {"GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
          "TGT": "C", "TGC": "C",
          "GAT": "D", "GAC": "D",
          "GAA": "E", "GAG": "E",
          "TTT": "F", "TTC": "F",
          "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
          "CAT": "H", "CAC": "H",
          "ATA": "I", "ATT": "I", "ATC": "I",
          "AAA": "K", "AAG": "K",
          "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
          "ATG": "M", "AAT": "N", "AAC": "N",
          "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
          "CAA": "Q", "CAG": "Q",
          "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
          "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
          "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
          "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
          "TGG": "W",
          "TAT": "Y", "TAC": "Y",
          "TAA": "_", "TAG": "_", "TGA": "_"}
    protein = ''
    for i in range(0, len(seq) - 2, 3):
        cod = seq[i:i + 3]
        if cod not in tc:
            continue
        elif tc[cod] == "_":
            break
        else:
            protein += tc[cod]
    return -1 if protein == '' else len(protein)


def translate(cod):
    """Given a codon translate it using the codon table"""
    cod = cod.upper()
    tc = {"GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
          "TGT": "C", "TGC": "C",
          "GAT": "D", "GAC": "D",
          "GAA": "E", "GAG": "E",
          "TTT": "F", "TTC": "F",
          "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
          "CAT": "H", "CAC": "H",
          "ATA": "I", "ATT": "I", "ATC": "I",
          "AAA": "K", "AAG": "K",
          "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
          "ATG": "M", "AAT": "N", "AAC": "N",
          "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
          "CAA": "Q", "CAG": "Q",
          "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
          "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
          "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
          "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
          "TGG": "W",
          "TAT": "Y", "TAC": "Y",
          "TAA": "_", "TAG": "_", "TGA": "_"}
    return tc[cod] if cod in tc else None


# Define the whole translation
def translation(seq):
    """Given a seq return the translated protein"""
    protein = ''
    for pos in range(0, len(seq) - 2,3):
        cod = seq[pos:pos + 3]
        protein += translate(cod)
    return protein


def istranslatable(aa_seq):
    """Returns a logic value if the seq can be a protein or not"""
    if not translate(aa_seq):  # handle edge case here.......
        return False
    else:
        return True


def trans_map(seq):
    """Maps amino acids frequencies with the seq translation """
    seq = seq.upper()
    prot = ''
    result = {}
    for pos in range(0, len(seq) - 2, 3):
        cod = seq[pos:pos + 3]
        if translate(cod) == "_":
            continue
        else:
            prot += translate(cod)
    unique = []
    for aa in prot:
        if aa not in unique:
            unique.append(aa)
    for i in unique:
        result.update({f'{i}': prot.count(i)})
    return result


def dna_subseq(seq, aa):
    """Reads an AA & DNA seq & prints list of all sub_seqs of DNA seq that encode given aa seq"""
    seq = seq.upper()
    subseqs = []
    aa_seq = ''
    for pos in range(0, len(seq) - 2):
        cod = seq[pos:pos + 3]
        if translate(cod) == '_':
            subseqs.append(aa_seq)  # if stop codon exists tu
            aa_seq = ''
        else:
            aa_seq += translate(cod)

    return subseqs


print(dna_subseq('atggtacaaatcgtcctgatt', 'IVPL'))
print(translation('atcggtacaaatggtcctgatt'))
