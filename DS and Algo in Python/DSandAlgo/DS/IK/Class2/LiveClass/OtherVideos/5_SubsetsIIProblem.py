def subsetII(nums):
    result = list()

    def helper(nums, idx, slate):

        if idx == len(nums):
            result.append(slate[:])
            return
        else:
            count = 0
            for pick in range(idx, len(nums)):
                if nums[pick] != nums[idx]:
                    break
                count += 1

            helper(nums, idx + count, slate)

            for c in range(1, count+1):
                slate.append(nums[idx])
                helper(nums, idx + count, slate)

            for c in range(1, count+1):
                slate.pop()

    nums.sort()
    helper(nums, 0, [])
    return result


st = [1, 2, 2]
print(subsetII(st))
