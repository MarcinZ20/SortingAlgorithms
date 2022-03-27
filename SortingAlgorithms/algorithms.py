import numpy as np
import operator 

availableAlgorythms = {
        1: "Bubble Sort",
        2: "Insertion Sort",
        3: "Selection Sort",
        4: "Merge Sort",
        5: "Quick Sort",
        6: "Heap Sort",
        7: "Bucket Sort",
        8: "Counting Sort",
        9: "Position Sort"
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
        


                ##### ---------------------------- TODO: Zadanie 2 ---------------------------- #####


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

def heapSort(table: np.ndarray) -> None:
    """
        A function to represent Heap sort algorithm   

    Args:
        table (np.ndarray): array to be sorted
    """

    length = len(table)
  
    for i in range(length//2, -1, -1):
        heapify(table, length, i)
  
    for i in range(length-1, 0, -1):
        table[i], table[0] = table[0], table[i]
        heapify(table, i, 0)

def heapify(table: int, length: int, head: int):
    """
        A function to represent heapify part of heap sort algorithm   

    Args:
        table (np.ndarray): array to be sorted
        length (int): length of the array part
        head (int): head node 
    """
    
    left = 2 * head + 1 
    right = 2 * head + 2 

    values = {head: table[head]}

    if left < length:
        values[left] = table[left]

    if right < length:
        values[right] = table[right]

    largest = max(values.items(), key=operator.itemgetter(1))[0]

    # If root is not largest, swap with largest and continue heapifying
    if largest != head:
        table[head], table[largest] = table[largest], table[head]
        heapify(table, length, largest)

def bucketSort(table: np.ndarray) -> None:
    """
        A function to represent Bucket sort algorithm   

    Args:
        table (np.ndarray): array to be sorted
    """

    max_number = np.max(table)

    # Ustalam rozmiar bucketow
    size = max_number / len(table)

    buckets = [[] for i in range(len(table))]

    # wkładam elementy do odpowiednich bucketow
    for number in table:

        bucketIndex = int(number // size)

        if (bucketIndex >= len(table)):
            buckets[bucketIndex - 1].append(int(number))
        else:
            buckets[bucketIndex].append(int(number))

    # sortuje buckety
    for bucket in buckets:
        insertionSort(bucket)

    # dodaje odpowiednio w kolejnosci elementy do tablicy
    tableIndex = 0

    for bucket in buckets:
        for number in bucket:
            table[tableIndex] = number
            tableIndex += 1


def countingSort(table: np.ndarray) -> None:
    """
        A function to represent Counting Sort algorithm    

    Args:
        table (np.ndarray): array to be sorted
    """

    maximum = max(table)

    indexTab = np.zeros(maximum + 1)

    for number in table:
        indexTab[number] += 1

    tabPointer = 0

    for index, value in enumerate(indexTab):
        if value != 0:
            for _ in range(int(value)):
                table[tabPointer] = index
                tabPointer += 1

def positionSort(table: np.ndarray):
    """
        A function to represent Position sort algorithm   

    Args:
        table (np.ndarray): array to be sorted
    """

    maxItem = np.max(table)

    numberOfDigits = len(str(maxItem))

    index = 1

    for i in range(numberOfDigits):
        countingSortForRadix(table, index)
        index *= 10

def countingSortForRadix(table: np.ndarray, sigIndex: int):
    """
        A helper function to the one above (position sort)
    Args:
        table (np.ndarray): array to be sorted
        index (int): index of most significant digit
    """
 
    length = len(table)
 
    output = list(np.zeros(length))
    count = list(np.zeros(10))
 
    for i in range(0, length):
        index = table[i] // sigIndex
        count[index % 10] += 1
 
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    for k in range(length - 1, -1, -1):
        index = table[k] // sigIndex
        output[int(count[index % 10] - 1)] = table[k]
        count[index % 10] -= 1

    for j in range(0, len(table)):
        table[j] = output[j]
