def merge_sorted(arr1,arr2):
    sorted_arr = []
    i,j =0,0
    #print(f'Before: (i) {i} value {arr1[i]}')
    #print(f'Before: (j) {j} value {arr2[j]}')
    while i < len(arr1) and j < len(arr2):
        #print(f'After : (i) {i} value {arr1[i]}')
        #print(f'After : (j) {j} value {arr2[j]}')
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
        print(f'sorted arr {sorted_arr}')

    #print(f'for i : {i != len(arr1)}')
    #print(f'for j : {j != len(arr2)}')
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    return sorted_arr

# l1 = [1,4,6,8]
# l1 = [1,4,6,8,11,15,16]
l1 = []
l2 = [2,3,5,7,8,9,10]
print(f'merged list : {merge_sorted(l1,l2)}')
