from SortingAlgorithms import algorithms
from table import Table

class Algorithm():
    """A class to represent algorithm in the program

    Attributes
    ----------
    id: int
        algorithm id used to identify which one to use
    mame: str
        name of the used algorithm

    Methods
    -------
    __init__(self, id: int, name: None) -> None:
        creates object of type Algorithm and starts execusion of specific one

    @property
    id(self) -> int:
        returns id of the object

    @property
    name(self) -> str:
        returns name of the object

    @id.setter
    id(self, number: int):
        sets id of the object

    @name.setter
    name(self, name: str):
        sets name of the object (if not provided, the default name is created)

    @staticmethod
    createTable() -> Table:
        creates object of type Table with specified parameters

    startAlgorythm(self) -> None:
        starts execusion of specific sorting algorith (by default is called by function __init__())
    """

    id: int
    name: str

    def __init__(self, id: int, name = None) -> None:
        self.id = id
        self.name = name 
        self.startAlgorythm()

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @id.setter
    def id(self, number: int):
        self.__id = number

    @name.setter
    def name(self, name: str):
        self.__name = name if name is not None else algorithms.availableAlgorythms[self.id]

    @staticmethod
    def createTable() -> Table:
        while True:
            try:
                size = int(input("\nRozmiar tablicy: "))
            except (TypeError, ValueError):
                print("Nieprawidłowe dane - jeszcze raz!")
            else:
                break


        decision = str(input("Chesz nazwac tablice (y/n)?: "))
        if decision.upper() == "Y":
            while True:
                try:
                    name = str(input("Nazwa tablicy: "))
                except (TypeError, ValueError):
                    print("Podaj nazwe w formacie: \"nazwa\"")
                else:
                    break
        else:
            name = f"tab_{Table._instanceCount + 1}"

        new_table = Table.initializeTable(size)
        print(f"Wygenerowana tablica: {new_table}")
        
        while True: 
            try:
                number = int(input("\nIle razy pomieszac tablice: "))
            except (TypeError, ValueError):
                print("Nieprawidłowe dane - jeszcze raz!")
            else:
                break

        if number != 0:
           Table.shuffleTable(number, new_table)

        table = Table(name, new_table, size)

        return table

    def startAlgorythm(self) -> None:

        table = Algorithm.createTable()
        array = table.array

        print(f"\n{table.name} przed sortowaniem: ")
        table.printTable()

        if self.id == 1:
            algorithms.bubbleSort(array)
        elif self.id == 2:
            algorithms.insertionSort(array)
        elif self.id == 3:
            algorithms.selectSort(array)
        elif self.id == 4:
            algorithms.mergeSort(array)
        elif self.id == 5:
            algorithms.quickSort(array, 0, len(array) - 1)
        elif self.id == 6:
            algorithms.heapSort(array)
        elif self.id == 7:
            algorithms.bucketSort(array)
        elif self.id == 8:
            algorithms.countingSort(array)
        elif self.id == 9:
            algorithms.positionSort(array)

        print(f"\n{table.name} po sortowaniu algorytmem {algorithms.availableAlgorythms[self.id]}: ")

        table.printTable()
