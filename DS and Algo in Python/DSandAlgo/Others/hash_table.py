# Table
# table = [None] * 10
from typing import List, Any

table: List[List[None]] = [[] for _ in range(10)]

# hash_function
def hash_function(k):
    return k%10

# insert
def hash_insert(table, key, value):
    #table[hash_function(key)] = value
    table[hash_function(key)].append(value)

print(table)
# print(hash_function(10))
hash_insert(table, 5, 'Apple')
# print(table)
hash_insert(table, 117, 'Orange')
# print(table)
hash_insert(table, 115, 'Pineapple')
print(table)