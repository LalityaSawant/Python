def driver(nums):
    result = []
    helper(nums, 0,result)
    
def helper(nums, idx, partsol, result):
    # base 
    partsol = []
    if idx == len(nums):
        result.add(partsol)
    else:
        helper(nums,idx+1,partsol,result)
        partsol.append(nums(idx))