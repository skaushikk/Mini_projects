# from util import time_it
# import timing
import timer


# @ time_it
def merge(left, right):
    res = []
    lp = rp = 0

    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            res.append(left[lp])
            lp += 1
        else:
            res.append(right[rp])
            rp += 1

    res.extend(left[lp:])
    res.extend(right[rp:])

    return res

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return merge(left, right)


import random


# @ time_it
def quicksort(array):
    if len(array) <= 1:
        return array
    pivot0 = random.choice(array)
    array.remove(pivot0)
    ll = []
    lr = []
    for i in array:
        if i <= pivot0:
            ll.append(i)
        else:
            lr.append(i)
    return quicksort(ll) + [pivot0] + quicksort(lr)

def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j
        while i > 0 and array[i-1] > key:
            array[i] = array[i-1]
            i -= 1
        array[i] = key


def main():
    array = [5, 4, 3, 2, 1, 6, 7, 8, 54]
    print(array)

    # result = merge_sort(array)
    # result = quicksort(array)
    result = insertion_sort(array)
    print(result)


if __name__ == '__main__':
    main()
