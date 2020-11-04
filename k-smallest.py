import random
import timer


def findKsmallest(nums, k):
    def partition(left, right):
        pivot = nums[right]
        # nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        start_idx = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[start_idx], nums[i] = nums[i], nums[start_idx]
                start_idx += 1
        nums[right], nums[start_idx] = nums[start_idx], nums[right]
        return start_idx

    def select(left, right, k_smallest):
        """
        Returns the k-th smallest element of list within left..right
        """
        if left == right:  # If the list contains only one element,
            return nums[left]  # return that element

        # select a random pivot_index between
        # pivot_index = random.randint(left, right)

        # find the pivot position in a sorted list
        pivot_index = partition(left, right)

        # the pivot is in its final sorted position
        if k_smallest == pivot_index:
            return nums[k_smallest]
        # go left
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        # go right
        else:
            return select(pivot_index + 1, right, k_smallest)

    return select(0, len(nums) - 1, k - 1)


A = [1, 3, 5, 6, 8, 7, 4, 2, 9]
k = 3

print(kthsmallest(A, k))
print(findKsmallest(A, k))

print(sorted(A))
import heapq


def kthsmallest(nums, k):
    return heapq.nlargest(len(nums) - k + 1, nums)[-1]


"""
Sort a string according to the order defined by another string
"""


def string_sort_pattern(pat, s):
    pat_dict = {}
    for i, p in enumerate(pat):
        pat_dict[p] = i
    res = ''
    s = sorted(s, key = lambda ele: pat_dict[ele])
    return ''.join(s)

pat = 'bvyzca'
s = 'abcabcabc'
print(string_sort_pattern(pat, s))