def subset_of_n(n):
    if n == 0:
        return 1
    else:
        return 2 * subset_of_n(n-1)


def subset_of_n_divide(n):
    # O(2^n) -- does exponential amount of work here n = 5 then 2^n = 32 so lot of more work than O(n)
    if n == 0:
        return 1
    else:
        return subset_of_n_divide(n-1) + subset_of_n_divide(n-1)


# ToDO: subset_of_n_decrease_by_factor solution
# if( N == 0)
#     return 1;
# else if (N is odd)
# return 2 * (2^(N/2))^2
# else
# return (2^(N/2))^2

def subset_of_n_decrease_by_factor(n):
    if n == 0:
        return 1
    elif n % 2 != 0:
        return 2 * subset_of_n_decrease_by_factor(n//2)
    else:
        return 2 ** subset_of_n_decrease_by_factor(n//2)


s = 5
# print(subset_of_n(s))
# print(subset_of_n_divide(s))
print(subset_of_n_decrease_by_factor(s))
