def binarystring(n):
    # BFS: breadth first search
    if n == 1:
        return['0', '1']
    else: # n>1
        prev = binarystring(n-1)
        result = []
        for s in prev:
            result.append(s + '0')
            result.append(s + '1')
        return result


def binarystring_itr(n):
    # BFS: breadth first search
    result = ['0', '1']
    for i in range(2, n+1):
        newresult = []
        for s in result:
            newresult.append(s+'0')
            newresult.append(s+'1')
        result = newresult

    return result


def binarystring_final(n):
    binarystring_final_helper("", n)


def binarystring_final_helper(slate, n):
    # DFS: depth first search
    if n == 0:
        print(slate)
    else:
        binarystring_final_helper(slate+'0', n-1)
        binarystring_final_helper(slate+'1', n-1)


num = 3
print(binarystring(num))
print(binarystring_itr(num))
binarystring_final(num)

