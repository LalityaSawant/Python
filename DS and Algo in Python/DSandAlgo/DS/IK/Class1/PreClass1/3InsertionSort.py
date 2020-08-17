def insertion_sort(nums):

    for i in range(1, len(nums)):
        j = i - 1
        curr = nums[i]

        while j >= 0 and nums[j] > curr:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = curr
        print(nums)

    return nums


ar = [5, 3, 1, 2, 4, 7, 6, 8, 6, -1]

insertion_sort(ar)
print(ar)
