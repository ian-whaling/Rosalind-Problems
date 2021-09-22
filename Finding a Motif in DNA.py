positions = []
with open("rosalind_subs.txt", 'r') as file:
    dna_strings = file.read().split('\n')
    string = dna_strings[0]
    substring = dna_strings[1]
    for i in range(len(string) - len(substring)):
        if string[i:i + len(substring)] == substring:
            positions.append(i + 1)
print(*positions)