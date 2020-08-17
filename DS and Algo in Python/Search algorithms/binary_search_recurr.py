def bisection_recur(n,arr,start,stop):
    if start > stop:
        return f'{n} not found in list'
    else:
        mid = (start+stop)//2
        if n == arr[mid]:
            return f"{n} found at index: {mid}"
        elif n > arr[mid]:
            start = mid + 1
            return bisection_recur(n,arr,start,stop)
        else:
            stop = mid - 1
            return bisection_recur(n,arr,start,stop)

def create_list(max_val):
    arr = []
    for num in range(1,max_val):
        arr.append(num)
    return arr

l = [1,2,3,4,5,6,7,8,9,10]
#ind 0 1 2 3 4 5 6 7 8 9

#l = create_list(10)

for num in range(16):
    print(bisection_recur(num,l,0,len(l)-1))
