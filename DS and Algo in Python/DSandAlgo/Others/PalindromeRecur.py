def pal_recur(s):
    itr = 0
    if len(s) <= 1:
        return True
    else:
        itr += 1
        return s[0] == s[len(s)-1] and pal_recur((s[itr:(len(s) - 1) - itr]))

# wasitacaroracatisaw
#  arora
print(pal_recur('abcba'))
