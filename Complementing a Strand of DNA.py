for dna in open("rosalind_revc.txt"):
    rev_dna = list(dna[::-1])[1:]
    for i in range(len(rev_dna)):
        if rev_dna[i] == "A":
            rev_dna[i] = "T"
            continue
        elif rev_dna[i] == "T":
            rev_dna[i] = "A"
            continue
        elif rev_dna[i] == "C":
            rev_dna[i] = "G"
            continue
        else:
            rev_dna[i] = "C"
    print("".join(rev_dna))
    