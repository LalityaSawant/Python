def recur_fibonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recur_fibonachi(n-1) + recur_fibonachi(n-2)

z = 10
print(recur_fibonachi(z))
