from heapq import merge
from posixpath import split
from turtle import right


def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Finds the midpoint of the list and divides into sublists
    Conquer: Recursiely sorts the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    Runs in O(nlog(n)) time
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    right = merge_sort(right_half)
    left = merge_sort(left_half)

    return merge(left, right)

def split(list):
    """
    Runs in O(log(n)) time
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    Runs in O(nlog(n)) time
    """
    
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])

alist = [54, 78, 9.2, 4, 65, 12.1, 32]

print(verify_sorted(alist))

print(merge_sort(alist))

l = merge_sort(alist)

print(verify_sorted(l))

