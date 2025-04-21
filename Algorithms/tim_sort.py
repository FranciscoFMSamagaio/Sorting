
def TimSort(data):
    minRun = 10
    n = len(data)

    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun, n)
        data[start:end] = sorted(data[start:end])

    size = minRun
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merged_array = merge(data[left:mid + 1], data[mid + 1:right + 1])
                data[left:left + len(merged_array)] = merged_array

        size *= 2

    return data