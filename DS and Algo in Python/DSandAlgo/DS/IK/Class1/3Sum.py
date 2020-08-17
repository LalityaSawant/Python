a = [-1, 0, 1, 2, -1, -4]

b = [0, 0, 0, 0]

c = [0, 0, 0]

d = [-1, 0, 1]

e = [1,-1,-1,0]

f = [10,3,-4,1,-6,9]

g = [12,34,-46]


# def threeSum(nums):
#     nums.sort()
#
#     oa = []
#     k = len(nums) - 1
#
#     for i in range(1, k):
#         j = i - 1
#         req_num = -(nums[i] + nums[j])
#
#         if nums[k] == req_num:
#             oa.append([nums[i], nums[j], nums[k]])
#             k -= 1
#
#         while req_num < nums[k] and k > i:
#             k -= 1
#
#         # while nums[i] == nums[j]:
#         #     k -= 1
#         #     i += 1
#
#     return oa
#
#
# def threeSum2(nums):
#     nums.sort()
#     oa = []
#
#     i = 1
#     j = i - 1
#     k = len(nums)-1
#
#     for i in range(len(nums)-1):
#         if i > 0 and nums[i] == nums[i-1]:
#             continue
#         j = i-1
#         k = len(nums)-1
#         while k > i:
#             sum = nums[i] + nums[j] + nums[k]
#             if sum == 0:
#                 oa.append([nums[i], nums[j], nums[k]])
#                 while i<len(nums)-1 and nums[i] == nums[i + 1]:
#                     i += 1
#                 while k>0 and nums[k] == nums[k - 1]:
#                     k -= 1
#                 i += 1
#                 k -= 1
#
#             elif 0 < nums[i] + nums[j] + nums[k]:
#                 k -= 1
#             else:  # 0 > nums[i] + nums[j] + nums[k]:
#                 i += 1
#
#     return oa
#
#
# def threeSum3(nums):
#     if len(nums) < 3:
#         return
#
#     nums.sort()
#     oa = []
#     i = 1
#     k = len(nums) - 1
#
#     while i < k:
#         j = i - 1
#         if nums[i] + nums[j] + nums[k] == 0:
#             oa.append([nums[j], nums[i], nums[k]])
#             i += 1
#             k -= 1
#         else:
#             i += 1
#             k -= 1
#
#     return oa
#
#
# def threeSum4(nums):
#     nums.sort()
#     result = []
#     for i in range(len(nums)-2):
#         if i > 0 and nums[i] == nums[i-1]:
#             continue
#         l = i+1
#         r = len(nums)-1
#         while(l<r):
#             sum = nums[i] + nums[l] + nums[r]
#             if sum<0:
#                 l+=1
#             elif sum >0:
#                 r-=1
#             else:
#                 result.append([nums[i],nums[l],nums[r]])
#                 while l<len(nums)-1 and nums[l] == nums[l + 1]:
#                     l += 1
#                 while r>0 and nums[r] == nums[r - 1]:
#                     r -= 1
#                 l+=1
#                 r-=1
#     return result

def sum3(A):
    A.sort()
    sum = 0
    oa = []
    for i in range(0, len(A)-1):
        if i > 0 and A[i] == A[i-1]:
            continue
        j = i + 1
        k = len(A) - 1
        while j < k:
            sum = A[i] + A[j] + A[k]
            if sum < 0:
                #k -= 1
                j += 1
            elif sum > 0:
                #j += 1
                k -= 1
            else:  # sum = 0
                #oa.append([A[i], A[j], A[k]])
                oa.append(f'{A[i]},{A[j]},{A[k]}')
                while A[k] == A[k-1] and k > i:
                    k -= 1
                while A[j] == A[j+1] and j < k:
                    j += 1
                j += 1
                k -= 1
    return oa

print(sum3(f))
