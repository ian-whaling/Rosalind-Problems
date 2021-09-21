def pairs(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return pairs(n - 1, k) + k*pairs(n - 2, k)
for line in open("rosalind_fib.txt"):
    n, k = map(int, line.split())
    print(pairs(n, k))