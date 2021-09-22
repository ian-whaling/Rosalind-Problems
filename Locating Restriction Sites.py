def reverse_complement(dna):
    rev_dna = list(dna[::-1])
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
    return ''.join(rev_dna)

output = []
with open("rosalind_revp.txt", 'r') as file:
    next(file)
    dna = file.read().replace('\n', '')

length = len(dna)
for i in range(length):
    for j in range(4, 13):
        if i + j > length:
            continue
        if dna[i:i+j] == reverse_complement(dna[i:i+j]):
            output.append((i + 1, len(dna[i:i+j])))

for i,j in output:
    print(i,j, sep = ' ', end='\n')