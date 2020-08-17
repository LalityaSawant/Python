def permutationsII(nums):
    result = list()

    def helper(nums, idx, slate):
        if idx == len(nums):
            return result.append(slate[:])
        else:
            dict_lookup = {}
            for pick in range(idx, len(nums)):
                if nums[pick] in dict_lookup:
                    continue
                else:
                    nums[pick], nums[idx] = nums[idx], nums[pick]
                    slate.append(nums[idx])
                    helper(nums, idx+1, slate)
                    slate.pop()
                    nums[pick], nums[idx] = nums[idx], nums[pick]
                    dict_lookup[nums[pick]] = nums[pick]

    helper(nums, 0, [])
    return result


st = [2,2,1,1]
print(permutationsII(st))
