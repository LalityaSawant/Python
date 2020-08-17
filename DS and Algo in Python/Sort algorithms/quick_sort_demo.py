def quick_sort(arr):
    '''
    Input: unsorted
    Output: sorted_arr
    Note: this is not inplace algorithm
    '''

    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1] #gets last element

        smaller, equal, larger = [], [], []

        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
    return quick_sort(smaller) + equal + quick_sort(larger)

l = [6,8,1,4,10,7,8,9,3,2,5]
print(quick_sort(l))
