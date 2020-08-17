def raise_ittr(base, power):
    result = 1
    for i in range(power):
        result *= base

    return result


print(raise_ittr(2, 3))


def raise_recur(base, power):

    if power == 0:
        return 1
    else:
        return base * raise_ittr(base, power - 1)


print(raise_ittr(2, 3))
