# mutable solution
def letter_case_problem(s):
    result = list()
    # helper(s, 0, '', result)
    # return result

    def helper(subp, idx, slate):
        digits = '0123456789'
        if idx == len(subp):
            return result.append(slate)
        else:
            if subp[idx] in digits:
                helper(subp, idx+1, slate + subp[idx])
            else:
                helper(subp, idx+1, slate + subp[idx].lower())
                helper(subp, idx+1, slate + subp[idx].upper())

    helper(s, 0, '')
    return result


# immutable solution
def letter_case_problem_immutable(s):
    result = list()
    # helper(s, 0, [], result)
    # return result

    def helper(subp, idx, slate):
        digits = '0123456789'
        if idx == len(subp):
            return result.append("".join(slate))
        else:
            if subp[idx] in digits:
                slate.append(subp[idx])
                helper(subp, idx+1, slate)
                slate.pop(idx)
            else:
                slate.append(subp[idx].lower())
                helper(subp, idx+1, slate)
                slate.pop(idx)

                slate.append(subp[idx].upper())
                helper(subp, idx+1, slate)
                slate.pop(idx)

    helper(s, 0, [])
    return result


st = 'a1b2'

print(letter_case_problem_immutable(st))
