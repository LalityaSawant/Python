def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_rabit(month):
    if month == 0:
        return 2
    elif month == 1:
        return 2
    else:
        return fib_rabit(month-1) + fib_rabit(month-2)


num = 5
for i in range(num+1):
    print(f'{i}: {fib(i)}')

months = 12
print(f'rabits after {months} months are: {fib_rabit(months)}')
