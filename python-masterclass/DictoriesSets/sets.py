farm_animals = {"Horse", "Cow", "Goat"}

for animal in farm_animals:
    print(animal)

print('-' * 40)

wild_animals = set(["Tiger", "Lion", "Leopard", "Elephant", "Giraffe"])

for animal in wild_animals:
    print(animal)

farm_animals.add("Horse")
wild_animals.add("Horse")

print(farm_animals)
print(wild_animals)

empty_set = set()
empty_set.add("a")
print(type(empty_set))
empty_set2 = {}  # will give dictionary and have error if we try adding to it
print(type(empty_set2))

even = set(range(0,45,2))
print(even)  # sets and dictionaries are ordered after python 3.6
print(type(even))
print(len(even))

squares_tuples = (4, 9, 16, 25, 36, 42)
squares = set(squares_tuples)
print(squares)
print(len(squares))

print("Union")
print(even.union(squares))
print(len(even.union(squares)))

print("Intersect")
print(even.intersection(squares))  # but sets are not ordered here in o/p
print(len(even.intersection(squares)))
print(even & squares)
print(sorted(even.intersection(squares)))
print(type(sorted(even.intersection(squares))))  # set concerted to list when sorted

print("Difference")
print(even - squares)  # set substractions
print(even.difference(squares))
print(squares.difference(even))
even.difference_update(squares)
print(even)

# just re establishing initial sets

even = set(range(0,45,2))

squares_tuples = (4, 9, 16, 25, 36, 42)
squares = set(squares_tuples)

print("Symmetric difference")
print(even.symmetric_difference(squares))
print(squares.symmetric_difference(even))

print("Discard and removed")
squares.discard(4)
squares.remove(9)
squares.discard(8)
print(sorted(squares))
# squares.remove(8) # will throw error if value not present

even = set(range(0,45,2))
squares = {4,6,16}

print("---Subset---")
print(squares.issubset(even))
if squares.issubset(even):
    print("squares is subset of even")

print("---Super set---")
print(even.issuperset(squares))
if even.issuperset(squares):
    print("even is superset of squares")

print("---FrozenSet---")
even = frozenset(range(0,43,2))
print(type(even))
print(even)


print("---- Challenge ----")
vowels = frozenset("aeiouAEIOU")

user_string_set = set(input("Enter any string: "))

print(sorted(user_string_set.difference(vowels)))


