# Shell Sort Algorithm
# This is a simple implementation of the Shell Sort algorithm in Python.
# Time Complexity: O(n log n)
# Space Complexity: O(1)

def ShellSort(data):
    n = len(data)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                yield data
                j -= gap
            data[j] = temp
            yield data
        gap //= 2
        yield data

    return data