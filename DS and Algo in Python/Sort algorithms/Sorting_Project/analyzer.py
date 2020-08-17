import random
import time
from demos import quick_sort,merge_sort,bubble_sort,insertion_sort,selection_sort

def create_random_list(size,max_val):
    ran_list = []
    for num in range(size):
        ran_list.append(random.randint(1,max_val))

    return ran_list

def analyze_func(func_name,arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    seconds = toc - tic
    print(f"{func_name.__name__.capitalize()}\t -> Elapsed time {seconds:.5f} ")

dasher = 40
size = int(input("what size list do you want to create? "))
max = int(input("what is the max value of the range? "))
run_times = int(input("How many times do you want to run? "))

for num in range(run_times):
    print(f'Run {num+1} results: ')
    print('-'*dasher)
    l = create_random_list(size,max)
    analyze_func(quick_sort,l)
    analyze_func(merge_sort,l)
    if len(l) <= 10000:
        analyze_func(selection_sort,l.copy())
        analyze_func(insertion_sort,l.copy())
        if len(l) <= 5000:
            analyze_func(bubble_sort,l.copy())
    analyze_func(sorted,l)
    print('-'*dasher)
    print('-'*dasher)
