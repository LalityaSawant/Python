a = [3, 2, 4]
k = 6


def twoSum(nums, target):
    nums.sort()

    i = 0
    j = len(nums)-1

    while j > i:
        req_num = target - nums[i]
        if nums[j] == req_num:
            return [nums[i], nums[j]]
        elif req_num < nums[j]:
            j -= 1
        else: # req_num > nums[j]:
            i += 1


#print(twoSum(a, k))

def twoSumHash(nums, target):
    dict = {}

    for i, num in enumerate(nums):
        req_num = target - num
        if req_num in dict:
            return dict[req_num], i
        else:
            dict[num] = i


print(twoSumHash(a, k))