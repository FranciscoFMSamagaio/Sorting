
def RadixSort(data):
    # Find the maximum number to know the number of digits
    max_num = max(data)

    # Initialize the exponent
    exp = 1

    # Perform counting sort for each digit
    while max_num // exp > 0:
        counting_sort(data, exp)
        exp *= 10
    return data

def counting_sort(data, exp):
    """
    A function to perform counting sort on the data based on the digit represented by exp.
    """
    n = len(data)
    output = [0] * n  # Output array
    count = [0] * 10  # Count array for digits (0-9)

    # Store the count of occurrences of each digit
    for i in range(n):
        index = (data[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (data[i] // exp) % 10
        output[count[index] - 1] = data[i]
        count[index] -= 1

    # Copy the output array to data[], so that data[] now contains sorted numbers
    for i in range(n):
        data[i] = output[i]
    yield data