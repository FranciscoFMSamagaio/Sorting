# Count Sort Algorithm
# This is a simple implementation of the Count Sort algorithm in Python.
# Time Complexity: O(n + k), where n is the number of elements in the input array and k is the range of the input values.
# Space Complexity: O(k), where k is the range of the input values.

def CountSort(data):
    # Find the maximum value in the data
    max_value = max(data)
    
    # Create a count array to store the count of each unique value
    count = [0] * (max_value + 1)
    
    # Store the count of each number in the count array
    for num in data:
        count[num] += 1
    
    # Reconstruct the sorted data
    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            data[index] = i
            index += 1
            count[i] -= 1
            yield data
    yield data