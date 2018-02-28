def bubble_sorted(iterable):
    new_list = list(iterable)
    list_len = len(new_list)
    for i in range(list_len - 1):
        for j in range(list_len - 1, i, -1):
            if new_list[j] < new_list[j - 1]:
                new_list[j], new_list[j - 1] = new_list[j - 1], new_list[j]
    return new_list

def insertion_sort(lst):
    if len(lst) == 1:
        return lst

    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp
    return lst

def quicksort(lst, lo, hi):
    if lo < hi:
        p = partition(lst, lo, hi)
        quicksort(lst, lo, p)
        quicksort(lst, p+1, hi)
    return lst

def partition(lst, lo, hi):
    pivot = lst[hi-1]
    i = lo - 1
    for j in range(lo, hi):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    if lst[hi-1] < lst[i+1]:
        lst[i+1], lst[hi-1] = lst[hi-1], lst[i+1]
    return i+1

def mergesort(li):
    if len(li) <= 1:
        return li

    return merge(mergesort(li[: len(li) / 2]), mergesort(li[len(li) / 2:]))

def merge(left, right):
    out = []
    while left and right:
        if left[0] <= right[0]:
            out.append(left.pop(0))
        else:
            out.append(right.pop(0))
    out.extend(left or right)
    return out

print mergesort([1,3,5,1,3,1,-1,6,2])
print merge([1,3,5], [2,4,6])
print merge([], [2,4,6])
print merge([1,2,3], [4,6])
print merge([2,9,11], [2,4,11,14])