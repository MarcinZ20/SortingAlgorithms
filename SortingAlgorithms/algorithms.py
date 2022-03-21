import numpy as np

availableAlgorythms = {
        1: "Bubble Sort",
        2: "Insertion Sort",
        3: "Selection Sort",
        4: "Merge Sort"
    }
    

def bubbleSort(table: np.ndarray) -> None:
    """
        A function to represent Bubble Sort algorithm.    

    Args:
        table (np.ndarray): array to be sorted
    """
    for i in range(0, len(table) - 1):
        for j in range(1, len(table)):
            if table[j - 1] > table[j]:
                x = table[j - 1]
                table[j - 1] = table[j]
                table[j] = x


def insertionSort(table: np.ndarray) -> None:
    """
        A function to represent Insertion Sort algorithm.    

    Args:
        table (np.ndarray): array to be sorted
    """
    for i in range(1, len(table)):
        key = table[i]
        j = i - 1
        while j >= 0 and key < table[j]:
            table[j+1] = table[j]
            j -= 1
        table[j+1] = key


def selectSort(table: np.ndarray) -> None:
    """
        A function to represent Selection Sort algorithm.    

    Args:
        table (np.ndarray): array to be sorted
    """
    for i in range(len(table)):
        min = table[i]
        min_index = i
        border = i + 1
        for index, value in enumerate(table[border:]):
            if value < min:
                min = value
                min_index = index + border
        
        table[min_index] = table[i]
        table[i] = min


def mergeSort(table: np.ndarray):
    """
        A function to represent Merge Sort algorithm    

    Args:
        table (np.ndarray): array to be sorted
    """

    if len(table) > 1:
        mid = len(table)//2

        left = np.array(table[:mid])
        right = np.array(table[mid:])

        mergeSort(left)
        mergeSort(right)

        l = c = r = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                table[c] = left[l]
                l += 1
            else:
                table[c] = right[r]
                r += 1
            c += 1

        while l < len(left):
            table[c] = left[l]
            l += 1
            c += 1

        while r < len(right):
            table[c] = right[r]
            r += 1
            c += 1
            