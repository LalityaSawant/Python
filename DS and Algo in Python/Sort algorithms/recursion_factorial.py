def recur_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

num = 0
print(recur_factorial(num))
