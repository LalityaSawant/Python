def raise_to_power(n, k):
    if k == 0:
        return 1
    else:
        return n * raise_to_power(n, k-1)


def raise_to_power_itr(n, k):
    result = 1
    for i in range(1,k+1):
        result = result * n

    return result


n = 6
k = 3

print(raise_to_power(n, k))
print(raise_to_power_itr(n, k))
