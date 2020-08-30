def fib(n):
    memo = {}
    memo[0] = 0
    memo[1] = 1
    if n in memo:
        return memo[n]

    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]


def fib_space(n):
    memo = {}
    memo[0] = 0
    memo[1] = 1
    if n in memo:
        return memo[n]

    for i in range(2, n+1):
        memo[i%3] = memo[(i-1)%3] + memo[(i-2)%3]

    return memo[n%3]


print(fib_space(6))
