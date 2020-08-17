def fibonacci(n):
    """ F(n) = F(n-1) + F(n-2) """
    if n < 2:
        return n
    else:
        # n = fibonacci(n-1) + fibonacci(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_eff(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus1 + n_minus2
            n_minus2 = n_minus1
            n_minus1 = result
    return result


for i in range(30):
    print('{:2} : {:8} \t {:8} '.format(i, fibonacci(i), fibonacci_eff(i)))


