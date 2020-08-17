def merger_first_into_second(arr1, arr2):
    i = 0
    j = 0
    oa = []

    while i < len(arr1) and j < len(arr2) and arr2[j] >= 1:
        if arr1[i] < arr2[j]:
            oa.append(arr1[i])
            i += 1
        else:
            oa.append(arr2[j])
            j += 1

    while i < len(arr1):
        oa.append(arr1[i])
        i += 1

    while j < len(arr2) and arr2[j] != 0:
        oa.append(arr2[j])
        j += 1

    arr2 = oa
    return(arr2)

arr1 = [1,3,5]

arr2 = [2,4,6,0,0,0]

print(merger_first_into_second(arr1, arr2))


