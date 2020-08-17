class AlgoHashTable:#dictories

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

hash_table = AlgoHashTable(256)
with open("data.txt") as f:
    #print(f.readline())
    for line in f:
        #line = f.readline().split(":")
        key,value = line.split(':')
        #print("key:", key,"value:", value)
        hash_table.set_val(key,value)

#print(hash_table)
print(hash_table.get_val('hvtybqabme@yaexample.com'))
print(hash_table.get_val('mashrur@example.com'))
print(hash_table.get_val('evgeny@example.com'))
