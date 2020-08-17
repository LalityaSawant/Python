def divide_arr(arr):
    #print('----------------------')
    #print('Arr length: ', len(arr))
    if len(arr) < 2:
        print(f'Base reached with {arr[:]}')
        return arr[:]
    else:
        middle = len(arr)//2 # gives whole number
        #print('middle: ', middle)
        print('Left: ', arr[:middle])
        print('Right: ', arr[middle:])
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])
        # implied return None

l = [2,3,4,5,6]
divide_arr(l)
