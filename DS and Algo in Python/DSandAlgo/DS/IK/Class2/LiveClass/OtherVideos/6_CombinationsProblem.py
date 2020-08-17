def combinations(nums, k):
    result = list()

    def helper(nums, idx, slate):
        if len(slate) == k:
            return result.append(slate[:])

        if idx == len(nums):
            return #result.append(slate[:])
        else:
            # exclude
            helper(nums, idx+1, slate)

            # include
            slate.append(nums[idx])
            helper(nums, idx+1, slate)
            slate.pop()

    helper(nums, 0, [])
    return result


st = [1, 2, 3]
print(combinations(st, 2))
