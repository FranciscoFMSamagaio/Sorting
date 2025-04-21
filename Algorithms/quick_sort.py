# Quick Sort Algorithm
# This is a simple implementation of the Quick Sort algorithm in Python.
# Time Complexity: O(n log n) on average, O(n^2) in the worst case
# Space Complexity: O(log n) due to recursion stack

def QuickSort(data):
    if len(data) <= 1:
        yield data
    else:
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        
        yield from QuickSort(left)
        yield middle
        yield from QuickSort(right)
