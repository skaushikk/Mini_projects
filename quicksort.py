import random
import timing

def quicksort(L):
    if len(L) <= 1:
        return L
    pivot0 = random.choice(L)
    L.remove(pivot0)
    ll = []
    lr = []
    for i in L:
        if i <= pivot0:
            ll.append(i)
        else:
            lr.append(i)
    return quicksort(ll) + [pivot0] + quicksort(lr)


if __name__ == '__main__':
    numbers_list = [0, 9, 3, 8, 8, 2, 7, 5]
    print('the original list is {}'.format(numbers_list))
    print(f"The sorted list is {quicksort(numbers_list)}")
