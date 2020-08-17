def driver(n):
    helper("", n)


def helper(slate, n):
    if n == 0:
        print(slate)
    else:
        for i in range(0, 10):
            choice = str(i)
            helper(slate+choice, n-1)
            choice.strip(str(i))

driver(2)