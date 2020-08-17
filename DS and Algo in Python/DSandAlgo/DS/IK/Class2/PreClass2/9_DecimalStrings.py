def decimalstring_final(n):
    decimalstring_final_helper("", n)


def decimalstring_final_helper(slate, n):
    # DFS: depth first search
    if n == 0:
        print(slate)
    else:
        for i in range(0, 11):
            decimalstring_final_helper(slate+str(i), n-1)

num = 2
decimalstring_final(num)