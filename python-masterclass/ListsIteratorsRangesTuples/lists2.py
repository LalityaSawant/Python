list_1 = []
list_2 = list()
print("List1 : {}".format(list_1))
print("List2 : {}".format(list_2))

if list_1 == list_2:
    print("The lists are equal")

print(list("The lists are equal"))

even = [2, 4, 6, 8]

#another_even = even

another_even = list(even)
#another_even = sorted(even, reverse=True)

print(another_even is even)  # False
print(another_even == even)  # True

# == checks contains of list
# is check object / address pointing

another_even.sort(reverse=True)
print(even)


odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

print('-' * 30)

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)
    print('-' * 30)
