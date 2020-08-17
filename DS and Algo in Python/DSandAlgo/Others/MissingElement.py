# O(NlogN)
def missing_element(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]


def missing_element2(arr1, arr2):
    d = {}

    for num in arr2:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1

    for num2 in arr1:
        if num2 in d:
            d[num2] -= 1
        else:
            return num2


print(missing_element([5, 5, 7, 7], [5, 5, 7]))

print(missing_element2([1, 2, 3, 4], [3, 2, 4]))
