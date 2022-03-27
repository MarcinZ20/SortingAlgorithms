from itertools import count
import numpy as np
import random


class Table:
    """
        A class to represent array of numbers in the program

        Attributes
        ----------
        tableSize: int
            size of the array
        name: str
            name of the array
        array: np.ndarray
            array of numbers
        _instanceCount: int
            class variable to represent how many instances of the Table are in the project (used to assign default names)

        Methods
        -------
        __init__(self, name: str, array: list, tableSize: int) -> None:
            constructs new table with specified arguments

        @property
        tableSize(self) -> int:
            returns size of the table

        @property
        name(self) -> str:
            returns name of the table

        @property
        array(self) -> np.ndarray:
            returns array of numbers

        @tableSize.setter
        tableSize(self, size: int):
            sets size of the table

        @name.setter
        name(self, name: str):
            sets name of the table

        @array.setter
        array(self, table: list):
            sets array converting list object to np.ndarray object

        @staticmethod
        initializeTable(size: int) -> list:

        @staticmethod
        shuffleTable(times: int, array: np.ndarray) -> None:
            shuffles the array specified number of times
        
        printTable(self) -> None:
            prints the table in specified format: item -> item -> item ... -> item
    """
    
    tableSize: int
    name: str
    array: np.ndarray
    _instanceCount = 0

    def __init__(self, name: str, array: list, tableSize: int) -> None:
        self.name = name 
        self.array = array 
        self.tableSize = tableSize
        self._instanceCount += 1
        
    @property
    def tableSize(self) -> int:
        return self.__tableSize

    @property
    def name(self) -> str:
        return self.__name

    @property
    def array(self) -> np.ndarray:
        return self.__array

    @tableSize.setter
    def tableSize(self, size: int):
        self.__tableSize = size

    @name.setter
    def name(self, name: str):
        self.__name = name

    @array.setter
    def array(self, table: list):
        self.__array = np.array(table)

    @staticmethod
    def initializeTable(size: int) -> list:
        array = []

        for i in range(size):
            array.append(random.randint(0,100))

        return array

    @staticmethod
    def shuffleTable(times: int, array: np.ndarray) -> None:
        for i in range(times):
            random.shuffle(array)
            print(f"Przetasowanie {i+1}: {array}")

    def printTable(self) -> None:
        output = np.array2string(self.array, max_line_width=100, separator=" -> ")
        output = [i.replace('[', "").replace(']', "") for i in output]
        output = ''.join(output)
        print(output)
