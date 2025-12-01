def proteins(strand):
    codon_table = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP"
    }

    result = []

    # Gehe in Schritten von 3 durch das RNA-Strand
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]

        if codon_table[codon] == "STOP":
            break

        result.append(codon_table[codon])

    return result
