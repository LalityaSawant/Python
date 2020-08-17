# TODO: fix last move
def tower_of_hanoi(n, src, dst, aux):
    if n == 0:
        return "print no disc to transfer"

    if n == 1:
        print(f"move " + src[n-1] + " from src  to aux")
        swap_array_elem(n-1, src, dst)
    else:
        tower_of_hanoi(n-1, src, aux, dst)
        print(f"move " + src[n-1] + " from src to aux")
        swap_array_elem(n-1, src, aux)
        tower_of_hanoi(n-1, aux, dst, src)


def swap_array_elem(n, src, dst):
    src[n], dst[n] = dst[n], src[n]


n = 2
arr1 = ['A', 'B']
arr2 = ['0', '0']
arr3 = ['0', '0']

tower_of_hanoi(n, arr1, arr2, arr3)
print(arr1)
print(arr2)
print(arr3)