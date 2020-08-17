def fact(n):
    result = 1
    if n == 0:
        result = 1
    else:
        for i in range(1, n+1):
            print(i, ' * ', result)
            result *= i
    return result


def rec_fact(n):
    # n! = n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * rec_fact(n-1)


# print(fact(0))
# print(fact(1))
# print(fact(2))
# print(fact(3))
# print(fact(4))
# print(fact(5))
print(fact(6))
print('-' * 20)
print(rec_fact(6))
