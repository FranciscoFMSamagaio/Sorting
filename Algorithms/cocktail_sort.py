# Cocktail Sort Algorithm
# This is a simple implementation of the Cocktail Sort algorithm in Python.
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Cocktail Sort is a variation of Bubble Sort that sorts in both directions on each pass through the list.
# It is also known as Bidirectional Bubble Sort or Shaker Sort.

def CocktailSort(data):
    n = len(data)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
                yield data

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
                yield data

        start += 1

    return data