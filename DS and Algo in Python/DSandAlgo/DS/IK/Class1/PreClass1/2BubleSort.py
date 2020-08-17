def buble_sort(a):

    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]

    return


ar = [5, 3, 1, 2, 4, 7, 6, 8, 6, -1]

buble_sort(ar)
print(ar)
