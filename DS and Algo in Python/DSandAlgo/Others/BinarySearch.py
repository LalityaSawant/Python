def binary_search(a, s):

    if s == a[len(a)//2]:
        return True
    elif s < a[len(a)//2]:
        return binary_search(a[:len(a)//2], s)
    elif s > a[len(a)//2]:
        return binary_search(a[len(a)//2+1:], s)
    else:
        return False


ar = [1, 2, 3, 4, 6, 7, 8, 9]

print(binary_search(ar, 7))
