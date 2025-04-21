# Heap Sort Algorithm
# This is a simple implementation of the Heap Sort algorithm in Python.
# Time Complexity: O(n log n)
# Space Complexity: O(1)

def HeapSort(data):
    n = len(data)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)
        yield data

    # One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]  # Swap
        heapify(data, i, 0)

    return data

def heapify(data, n, i):    
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child index
    right = 2 * i + 2  # right child index

    # If left child is larger than root
    if left < n and data[left] > data[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and data[right] > data[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        data[i], data[largest] = data[largest], data[i]  # Swap

        # Recursively heapify the affected subtree
        heapify(data, n, largest)