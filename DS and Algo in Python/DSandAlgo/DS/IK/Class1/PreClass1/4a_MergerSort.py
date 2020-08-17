def helper(A, start, end):
    if start >= end:
        return A

    mid = (start + end) // 2

    helper(A, start, mid)
    helper(A, mid + 1, end)

    i = start
    j = mid + 1
    aux = []
    while i <= mid and j <= end:
        if A[i] <= A[j]:
            aux.append(A[i])
            i += 1
        else:
            aux.append(A[j])
            j += 1

    while i <= mid:
        aux.append(A[i])
        i += 1

    while j <= end:
        aux.append(A[j])
        j += 1

    A[start: end+1] = aux
    return A


def sortArray(nums):
    return helper(nums, 0, len(nums)-1)



a = [1,7,5,3]

print(sortArray(a))
