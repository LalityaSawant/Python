class AlgoHashTable:

    def __init__(self,size):
        self.size = size
        self.hash_table = self.create_buckets()
        #print(self.hash_table)

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self,key,value):
        hashed_key = hash(key)%self.size #10 for checking multiple upload with same has value
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index,record in enumerate(bucket):
            record_key,record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key: #key exist:
            bucket[index] = (key,value)
        else:
            bucket.append((key,value))

    def get_val(self,key):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index,record in enumerate(bucket):
            record_key,record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return 'No Record Found'

    def del_val(self,key):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index,record in enumerate(bucket):
            record_key,record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
            #return (f'{record_value} is deleted
            return (record_value, 'is deleted')
        else:
            return 'No Record Found to delete'

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table = AlgoHashTable(10)

# for testing insert and updates
print(hash_table)
# hash_table.set_val('mashrur@example.com','some value')
# print(hash_table)
# hash_table.set_val('johndoe@example.com','some other value')
# print(hash_table)
# hash_table.set_val('mashrur@example.com','I love python')
# print(hash_table)

#for testing search
hash_table.set_val('mashrur@example.com',{'first_Name':'Mashru','last_Name':'Hussain'})
hash_table.set_val('johndoe@example.com',{'first_Name':'John','last_Name':'Doe'})
hash_table.set_val('janedoe@example.com',{'first_Name':'Jane','last_Name':'Doe'})
hash_table.set_val('tyrion@example.com',{'first_Name':'Tyrion','last_Name':'Bad Advice'})
hash_table.set_val('evgeny@example.com',{'first_Name':'Evgeny','last_Name':'Barbarian'})
print(hash_table)
print(hash_table.get_val('tyrion@example.com'))
print(hash_table.get_val('lals@example.com'))
print(hash_table.del_val('tyrion@example.com'))
print(hash_table)
