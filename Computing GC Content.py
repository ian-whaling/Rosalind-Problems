answer = ""
answer_gc_content = 0
with open("rosalind_gc.txt", 'r') as file:
    dna_strings = file.read().replace('\n', '').split(">")[1:]
    for string in dna_strings:
        tag = string[:13]
        dna = string[13:]
        gc_content = (dna.count("C") + dna.count("G")) / len(dna)
        if gc_content > answer_gc_content:
            answer_gc_content = gc_content
            answer = tag
    print(answer, answer_gc_content * 100, sep = "\n")