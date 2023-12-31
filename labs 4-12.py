import random

#Сортировка методом прочесывания
def bubble_sort(lst, flag):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if (lst[j] > lst[j + 1]) == flag:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

#Вставками
def insertion_sort(lst, flag):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and ((lst[j] < lst[j - 1]) == flag):
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1
    return lst

#Посредством выбора
def selection_sort(lst, flag):
    for i in range(len(lst)):
        if flag:
            mn = lst.index(min(lst[i::]))
            lst[i], lst[mn] = lst[mn], lst[i]
        else:
            mx = lst.index(max(lst[i::]))
            lst[i], lst[mx] = lst[mx], lst[i]
    return lst

#Шелла
def shell_sort(lst, flag):
    last_index = len(lst)
    step = len(lst) // 2
    while step > 0:
        for i in range(step, last_index):
            j = i
            delta = j - step
            while delta >= 0 and (lst[delta] > lst[j]) == flag:
                lst[delta], lst[j] = lst[j], lst[delta]
                j = delta
                delta = j - step
        step //= 2
    return lst

#Быстрая
def quick_sort(nums, flag):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]
    e_nums = [q] * nums.count(q)
    r_nums = [n for n in nums if n > q]
    if flag == True:
        return quick_sort(l_nums, True) + e_nums + quick_sort(r_nums, True)
    else:
        return list(reversed(quick_sort(l_nums, True) + e_nums + quick_sort(r_nums, True)))

#Пирамидальная
def heap_sort(lst):
    for i in range(len(lst), -1, -1):
        heapify(lst, len(lst), i)

    for i in range(len(lst) - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)
    return lst

#Слиянием
def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        lefthalf = lst[:mid]
        righthalf = lst[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lst[k] = lefthalf[i]
                i = i + 1
            else:
                lst[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            lst[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            lst[k] = righthalf[j]
            j = j + 1
            k = k + 1
    return lst

# поразрядная сортировка
def radix_sort(lst):
    max_digits = max([len(str(x)) for x in lst])
    base = 10
    bins = [[] for _ in range(base)]
    for i in range(0, max_digits):
        for x in lst:
            digit = (x // base ** i) % base 
            bins[digit].append(x)
        lst = [x for queue in bins for x in queue]
        bins = [[] for _ in range(base)]
    return lst

list_ = [1, 0, 7, -5, 6, 4]
print(bubble_sort(list_, True))
list_ = [1, 0, 7, -5, 6, 4]
print(insertion_sort(list_, True))
list_ = [1, 0, 7, -5, 6, 4]
print(selection_sort(list_, True))
list_ = [1, 0, 7, -5, 6, 4]
print(shell_sort(list_, True))
list_ = [1, 0, 7, -5, 6, 4]
print(quick_sort(list_, True))
list_ = [1, 0, 7, -5, 6, 4]
print(heap_sort(list_))
list_ = [1, 0, 7, -5, 6, 4]
print(merge_sort(list_))
list_ = [1, 0, 7, -5, 6, 4]
print(radix_sort(list_))


#Внешняя многофазная 
import os
import heapq
import tempfile

def external_sort(input_file, output_file, chunk_size):
    # Read input_file in chunks and sort each chunk
    with open(input_file, 'r') as f:
        chunk = []
        chunk_count = 0
        while True:
            line = f.readline()

            if not line:
                break
            chunk.append(int(line))

            if len(chunk) == chunk_size:
                chunk.sort()

                with open(f'chunk_{chunk_count}.tmp', 'w') as chunk_file:
                    for num in chunk:
                        chunk_file.write(f"{num}\n")

                chunk_count += 1
                chunk = []

    # Merge the sorted chunks using heapq
    with open(output_file, 'w') as out_file:
        files = [open(f'chunk_{i}.tmp', 'r') for i in range(chunk_count)]
        merged = heapq.merge(*files, key=lambda x: int(x))
        for line in merged:
            out_file.write(line)
        for i in files: i.close()

    print(chunk_count)
    # Clean up temporary files
    for i in range(chunk_count):
        os.remove(f'chunk_{i}.tmp')

# Пример использования
external_sort('input.txt', 'output.txt', chunk_size=2)
