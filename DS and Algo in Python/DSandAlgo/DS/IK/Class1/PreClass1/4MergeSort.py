def merge_sort(a):

    if len(a) <= 1:
        return a

    mid = len(a)//2

    la = merge_sort(a[:mid])
    ra = merge_sort(a[mid:])
    
    return merge(la, ra)


def merge(la, ra):
    i = 0
    j = 0
    oa = []

    while i < len(la) and j < len(ra):
        if la[i] < ra[j]:
            oa.append(la[i])
            i += 1
        else:
            oa.append(ra[j])
            j += 1

    while i < len(la):
        oa.append(la[i])
        i += 1

    while j < len(ra):
        oa.append(ra[j])
        j += 1

    return oa


ar = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]

print(merge_sort(ar))
