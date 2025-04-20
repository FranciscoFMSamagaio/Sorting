# Python program to implement Bubble Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
# compares adjacent elements and swaps them if they are in the wrong order.
# The pass through the list is repeated until the list is sorted.
# The algorithm gets its name from the way larger elements "bubble" to the top of the list.
# It is not suitable for large data sets as its average and worst-case time complexity is quite high.
# It is, however, a simple algorithm to implement and understand.

def bubbleSort(data):
  for i in range(len(data)):
    for j in range(0, len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j+1] = data[j+1], data[j]
        yield data
