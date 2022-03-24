import numpy as np

availableAlgorythms = {
        1: "Bubble Sort",
        2: "Insertion Sort",
        3: "Selection Sort",
        4: "Merge Sort",
        5: "Quick Sort"
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


def mergeSort(table: np.ndarray) -> None:
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
            
def quickSort(table: np.ndarray, left: int, right: int) -> None:
    """
        A function to represent Quick Sort algorithm    

    Args:
        table (np.ndarray): array to be sorted
        left (int): starting index of an array
        right (int): ending index of an array
    """

    if left >= right:
        return 

    pivot = partition(table, left, right)
    quickSort(table, left, pivot - 1)
    quickSort(table, pivot + 1, right)


def partition(table: np.ndarray, left: int, right: int) -> int:
    """
        A function to represent partition part of quick sort algorithm   

    Args:
        table (np.ndarray): array to be sorted
        left (int): starting index of an array
        right (int): ending index of an array
    """

    pivot = table[right]
    j = left - 1

    for i in range(left, right+1):
        if table[i] <= pivot:
            j += 1
            table[i], table[j] = table[j], table[i]
    
    return j

