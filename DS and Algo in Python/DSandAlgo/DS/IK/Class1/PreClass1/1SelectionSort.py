# T(n) = O(n^2)
# S(n) = O(1)


def selection_sort(a):

    for i in range(len(a)):
        min_element = a[i]
        min_elem_index = i
        for j in range(i+1, len(a)):
            if a[j] < min_element:
                min_element = a[j]
                min_elem_index = j

        a[i], a[min_elem_index] = a[min_elem_index], a[i]

    return


unsorted_list = [3, 2, 4, 1, 5, 6, 4, 6, 7, 9, -1]

selection_sort(unsorted_list)
print(unsorted_list)
