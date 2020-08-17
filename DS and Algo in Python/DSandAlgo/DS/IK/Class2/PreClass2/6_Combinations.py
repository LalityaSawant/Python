def comb(n, k):
    if n <= 1 or k == 0 or k == n:
        return 1
    else:
        return comb(n - 1, k) + comb(n - 1, k - 1)


print(comb(6, 3))
