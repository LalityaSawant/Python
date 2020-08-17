# not understood
# ToDO: additive Seriese
def addseq(n, b1, b2):
    if n == 0:
        return b1
    else:
        result = addseq(n-1, b1, b1+b2)
        return result

num = 5
print(addseq(num, 0, 1))
