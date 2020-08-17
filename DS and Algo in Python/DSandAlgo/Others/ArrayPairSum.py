# O(n^2)
def pair_sum(arr, k):

    result = set()

    for i, num in enumerate(arr):
        # print('{}:{}'.format(i, num))
        for num2 in arr[i+1:]:
            # print(num2)
            if num + num2 == k:
                result.add((num, num2))

    for pair in result:
        print(pair)

    return len(result)


# O(n)
def pair_sum2(arr, k):

    if len(arr) < 2:
        return

    # sets for tracking
    seen = set()
    output = set()

    for num in arr:

        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    for pair in output:
        print(pair)

    return len(output)


print(pair_sum2([1, 3, 2, 2], 4))

print(pair_sum([1, 3, 2, 2], 4))
