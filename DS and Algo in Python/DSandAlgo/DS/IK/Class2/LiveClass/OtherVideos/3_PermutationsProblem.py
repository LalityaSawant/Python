def permutations(nums):
    result = list()

    def helper(nums, idx, slate):
        if idx == len(nums):
            return result.append(slate[:])
        else:
            for i in range(idx, len(nums)):
                nums[0], nums[i] = nums[i], nums[0]
                slate.append(nums[i])
                helper(nums, idx+1, slate)
                slate.pop()
                nums[0], nums[i] = nums[i], nums[0]

    helper(nums, 0, [])
    return result


st = [1, 2, 3]
print(permutations(st))
