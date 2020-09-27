def to_rna(dna_strand:str)->str:
    return dna_strand.replace("A","U").replace("T","A").replace("G","R").replace("C","G").replace("R","C")
