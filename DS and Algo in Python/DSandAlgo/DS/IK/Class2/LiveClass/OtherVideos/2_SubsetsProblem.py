def subsets(nums):
    result = list()
    helper(nums, 0, [], result)
    return result


def helper(s, idx, slate, result):
    if idx == len(s):
        return result.append(slate[:])
    else:
        helper(s, idx+1, slate, result)

        slate.append(s[idx])
        helper(s, idx+1, slate, result)
        slate.pop()


st = [1, 2, 3]

print(subsets(st))
