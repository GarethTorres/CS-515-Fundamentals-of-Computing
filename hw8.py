import random
import sys
sys.setrecursionlimit(1000000)

# Q1 (10 pts): Implement random_numbers_generator
def random_numbers_generator(num=1000, min=0, max=10000):
    random_list = []
    for i in range(0, num):
        n = random.randint(min, max)
        random_list.append(n)
    return random_list

print(random_numbers_generator(num=3))
print(random_numbers_generator(num=3, min=0, max=10))
print(random_numbers_generator(num=3, min=5, max=10))

#    Returns num of random elements
#    Precondition: num, min, max should be int, max should bigger than num
#random_numbers_generator(num=3), return [645, 23, 7512]
#random_numbers_generator(num=3, min=0, max=10), return [5, 3, 1]
#random_numbers_generator(num=3, min=5, max=10), return [6, 9, 7]

# Q2 (20 pts): Implement Insertion Sort
def insertion_sort(random_list):
    before_sort = random_list[:]
    for i in range(1, len(random_list)):
        target_element = random_list[i]
        j = i - 1
        while j >= 0 and random_list[j] > target_element:
            random_list[j + 1] = random_list[j]
            j -= 1
        random_list[j + 1] = target_element
    return before_sort,random_list

print(insertion_sort([645, 23, 7512]))
print(insertion_sort([5, 3, 1]))
print(insertion_sort([6, 9, 7]))

#    Returns random_list and sorted_list
# insertion_sort([645, 23, 7512]), return [645,23,7512], [23,645,7512]
# insertion_sort([5, 3, 1]), return [5, 3, 1], [1, 3, 5]
# insertion_sort([6, 9, 7]), return [6, 9, 7], [6, 7, 9]

# Q3 (20 pts): Implement Quick Sort (Use the first element as pivot)
def pivot_first(arr, start, end):
    pivot = start
    for i in range(start,end):
        if arr[i] < arr[end]:
            arr[i],arr[pivot] = arr[pivot],arr[i]
            pivot += 1
    arr[pivot],arr[end] = arr[end],arr[pivot]
    return pivot

def quick_sort_first(arr, start, end):
    if start >= end:
        return
    index_p = pivot_first(arr, start, end)
    quick_sort_first(arr, index_p + 1, end)
    quick_sort_first(arr, start, index_p - 1)

def Quick_sort_first(random_list):
    before_sort = random_list[:]
    quick_sort_first(random_list, 0, len(random_list) - 1)
    return before_sort,random_list

print(Quick_sort_first([645, 23, 7512]))
print(Quick_sort_first([5, 3, 1]))
print(Quick_sort_first([6, 9, 7]))

#    Returns random_list and sorted_list
# Quick_sort_first([645, 23, 7512]), return [645,23,7512], [23,645,7512]
# Quick_sort_first([5, 3, 1]), return [5, 3, 1], [1, 3, 5]
# Quick_sort_first([6, 9, 7]), return [6, 9, 7], [6, 7, 9]

# Q4 (30 pts): Implement Quick Sort(Use a random element in the list as pivot)

def pivot_random(arr, start ,end):
    random_pivot_index = random.randint(start,end)
    arr[end], arr[random_pivot_index] = arr[random_pivot_index], arr[end]
    pivot = start
    for i in range(start,end):
        if arr[i] < arr[end]:
            arr[i],arr[pivot] = arr[pivot],arr[i]
            pivot += 1
    arr[pivot],arr[end] = arr[end],arr[pivot]
    return pivot

def quick_sort_random(arr, start, end):
    if start >= end:
        return
    index_p = pivot_random(arr, start, end)
    quick_sort_random(arr, index_p+1, end)
    quick_sort_random(arr, start, index_p-1)

def Quick_sort_random(random_list):
    before_sort = random_list[:]
    quick_sort_random(random_list, 0, len(random_list) - 1)
    return before_sort,random_list

print(Quick_sort_random([645, 23, 7512]))
print(Quick_sort_random([5, 3, 1]))
print(Quick_sort_random([6, 9, 7]))

#    Returns random_list and sorted_list
# Quick_sort_random([645, 23, 7512]), return [645,23,7512], [23,645,7512]
# Quick_sort_random([5, 3, 1]), return [5, 3, 1], [1, 3, 5]
# Quick_sort_random([6, 9, 7]), return [6, 9, 7], [6, 7, 9]

import time

Start = time.time()
Random_list = random_numbers_generator(num=1000000, max=100000*10)
print('Generating random list, time{}'.format(time.time()- Start))

Start = time.time()
sorted_list = insertion_sort(Random_list)
print('Sort random list by insertion, time{}'.format(time.time()- Start))

Start = time.time()
sorted_list = Quick_sort_first(Random_list)
print('Sort random list by Quick Sort using the first as pivot,time{}'.format(time.time()- Start))

Start = time.time()
sorted_list = Quick_sort_random(Random_list)
print('Sort random list by Quick Sort using a random num as pivot,time{}'.format(time.time()- Start))



