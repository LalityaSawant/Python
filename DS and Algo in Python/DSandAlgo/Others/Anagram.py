def anagram(str1, str2):
    arr_a = []
    arr_b = []

    for letter in str1:
        if letter != ' ':
            arr_a.append(letter)

    for letter in str2:
        if letter != ' ':
            arr_b.append(letter)

    arr_a.sort()
    arr_b.sort()

    if arr_a == arr_b:
        return True

    return False


def anagram2(s1, s2):

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True


print(anagram('clint a eastwood', 'old west action'))
print(anagram2('clint a eastwood', 'old west action'))
