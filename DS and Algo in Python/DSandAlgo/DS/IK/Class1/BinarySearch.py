#problem : find x in array a
a = [1, 2, 3, 4, 5]
x = 2


def binary_search_itr(a, x): # a is sorted
    begin_index = 0
    end_index = len(a) - 1

    while begin_index <= end_index:
        mid_index = begin_index + (end_index - begin_index) // 2
        mid_value = a[mid_index]
        #print(f'low:{begin_index} high:{end_index} mid:{mid_index} mid_val:{mid_value} x:{x}')
        if x == mid_value:
            return mid_index
        elif x < mid_value:
            end_index = mid_index - 1
        else: # x > mid_value
            begin_index = mid_value + 1

    return None


print(binary_search_itr(a, 5))
