

with open ("original.txt",'a') as file_to_write:
    for num in range(1,13):
        for product in range(1,13):
            print("{} into {} is {}".format(num, product, num * product), file=file_to_write)
        print('-' * 20 , file=file_to_write)

