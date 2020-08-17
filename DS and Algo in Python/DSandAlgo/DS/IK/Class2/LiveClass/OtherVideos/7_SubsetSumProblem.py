# TODO: def combinationsII()
# Complete the function below.


def check_if_sum_possible(arr, k):
    result = False
    def derive_sum(arr):
        sum_op = 0
        for num in arr:
            sum_op = sum_op + num

        return sum_op

    def helper(arr, k, idx, slate):
        # barcktracking for sum
        if len(slate) > 0 and idx == len(arr):
            sum_here = derive_sum(slate)
            if sum_here == k:
                result = True

        if idx == len(arr):
            # do something to return true or false
            return
        else:
            helper(arr, k, idx+1, slate)

            slate.append(arr[idx])
            helper(arr, k, idx+1, slate)
            slate.pop()

    helper(arr, k, 0, [])
    return result


inpt = [2, 4, 8]
k = 6

print(check_if_sum_possible(inpt, k))




# def find_all_well_formed_brackets(n):
#     result = list()
#
#     def count_brackets(slate, bracket):
#         ct = 0
#         for i in slate:
#             if i == bracket:
#                 ct += 1
#         return ct
#
#     def helper(n, idx, slate):
#         if len(slate) != 0 and len(slate) % 2 == 0 and len(slate) == 2*n:
#             ls = count_brackets(slate, "(")
#             rs = count_brackets(slate, ")")
#             if ls == rs:
#                 result.append(slate[:])
#
#         if idx == n:
#             return
#         else:
#             for i in range(0, n):
#                 slate = slate + '('
#                 helper(n, idx+1, slate)
#
#                 slate = slate + ')'
#                 helper(n, idx+1, slate)
#
#     helper(n, 0, "")
#     return result
#
# num = 2
# print(find_all_well_formed_brackets(num))
