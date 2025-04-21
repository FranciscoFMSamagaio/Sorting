# Odd Even Sort
# This is a simple implementation of the Odd-Even Sort algorithm in Python.
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def Odd_Even_Sort(data):
    n = len(data)
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(1, n - 1, 2):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                is_sorted = False
            yield data

        for i in range(0, n - 1, 2):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                is_sorted = False
            yield data