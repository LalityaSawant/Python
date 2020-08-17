def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


def fact_itr(n):
    result = 1
    for i in range(1, n+1):
        result = result * i

    return result


n = 6
print(fact(n))
print(fact_itr(n))
