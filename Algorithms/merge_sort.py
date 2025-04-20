
# Merge Sort Algorithm
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Merge Sort is a divide-and-conquer algorithm that divides the input array into two halves,
# recursively sorts them, and then merges the sorted halves back together.

def MergeSort(Data):
    if len(Data) <= 1:
        return Data

    mid = len(Data) // 2
    yield MergeSort(Data[:mid])
    yield MergeSort(Data[mid:])
    yield merge(MergeSort(Data[:mid]), MergeSort(Data[mid:]))
    yield Data

# Function to merge two sorted arrays
def merge(left, right):
    result = []
    i = j = 0

    # Merge the two arrays while maintaining sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from the left array
    result.extend(left[i:])

    # Append any remaining elements from the right array
    result.extend(right[j:])

    return result
