# Selection Sort Algorithm
# Time Complexity: O(n^2)
# Space Complexity: O(1)    
# Selection Sort is a simple and intuitive sorting algorithm that divides the input list into two parts:
# a sorted part and an unsorted part. It repeatedly selects the smallest (or largest, depending on the order)
# element from the unsorted part and moves it to the end of the sorted part.

def SelectionSort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        yield data