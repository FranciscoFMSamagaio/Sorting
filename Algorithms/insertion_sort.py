# This is a simple implementation of the Insertion Sort algorithm in Python.
# Time Complexity: O(n^2)
# Space Complexity: O(1)    

def InsertionSort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        yield data