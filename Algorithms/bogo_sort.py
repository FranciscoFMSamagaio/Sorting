'''
    Bogo Sort is a highly inefficient sorting algorithm that works by randomly shuffling the list
    until it is sorted. It is primarily used for educational purposes or as a joke algorithm.
    
    Complexity:
        - Worst case: O(∞)
'''
import random

def bogo_sort(data):
    def is_sorted(data):
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                return False
        return True

    while not is_sorted(data):
        random.shuffle(data)
        yield data  
        