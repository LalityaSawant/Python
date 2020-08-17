def quick_sort(a):
    quick_sort_helper(a, 0, len(a)-1)


def quick_sort_helper(a, low, hi):
    if low < hi:
        p = partition(a, low, hi)
        quick_sort_helper(a, low, p-1)
        quick_sort_helper(a, p+1, hi)


def get_pivot(a, low, hi):
    mid = (hi + low) // 2
    pivot = hi

    if a[low] < a[mid] < a[hi]:
        pivot = mid
    elif a[low] < a[hi]:
        pivot = low

    return pivot


def partition(a, low, hi):
    pivot_index = get_pivot(a, low, hi)
    pivot_value = a[pivot_index]
    a[pivot_index], a[low] = a[low], a[pivot_index]
    border = low

    for i in range(low, hi+1):
        if a[i] < pivot_value:
            border += 1
            a[i], a[border] = a[border], a[i]

    a[low], a[border] = a[border], a[low]

    return border


l = [2, 4, 5, 1, 3]

quick_sort(l)
print(l)