# Gnome Sort
# This is a simple implementation of the Gnome Sort algorithm in Python.
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def GnomeSort(data):
    index = 0
    while index < len(data):
        if index == 0 or data[index] >= data[index - 1]:
            index += 1
        else:
            data[index], data[index - 1] = data[index - 1], data[index]
            index -= 1
        yield data
    return data