from algorithm import Algorithm
import os
from sys import platform


class Menu:
    """
        A class to represent menu interface in the program.

        Attributes
        ----------
        inputList: list
            list of possible user inputs
        mainScreenMessage: str
            message that appears everytime program starts or repeats

        Methods
        -------
        __init__(self):
            creates object of type Menu and calls function to display entry informations

        displayMenu(self) -> None:
            displays mainScreenMessage

        cleanWindow(self) -> None:
            cleans terminal window after each execusion

        chooseSortingAlgorythm(self) -> int:
            determines which sorting algorithm one wants to use and returns value later used as a key to call specific function

        askToRepeat(self) -> bool:
            determines if at the end of the program, one wants to use it again - if so, returns True, else returns False
            
        @staticmethod
        start() -> None:
            static method containing main program loop
    """

    inputList = [1,2,3,4,5,7,8]
    mainScreenMessage = """
    - - - - - - - - - - - - - - - - - - -
    
    Wybierz algorytm sortowania: 

    1 -> Bubble Sort
    2 -> Insertion Sort
    3 -> Select Sort
    4 -> Merge Sort
    5 -> Quick Sort
    6 -> Heap Sort
    7 -> Bucket Sort
    8 -> Counting Sort
    
    - - - - - - - - - - - - - - - - - - -
    """
    
    def __init__(self) -> None:
        self.displayMenu()
        
    def displayMenu(self):
        print(self.mainScreenMessage)

    def cleanWindow(self):
        if platform in ["darwin", "linux", "linux2"]:
            command = "clear"
            os.system(command)
        else:
            command = "cls"
            os.system(command)

    def chooseSortingAlgorythm(self) -> int:
        number: int

        while True:
            try:
                number = int(input("Wybieram: "))
            except (ValueError, TypeError):
                print("Niepoprawne dane - jeszcze raz: ")
            else:
                if number not in self.inputList:
                    print("Niepoprawna wartosc jeszcze raz: ")
                else:
                    break

        return number
    
    def askToRepeat(self) -> bool:
        decision = str(input("\nCzy chcesz zaczac od nowa (y/n)?: ")) 

        if decision.upper() == "Y":
            return True
        else:
            print("Koniec programu! :)")
            return False

    @staticmethod
    def start() -> None:
        while True:
            menu = Menu()
            x = menu.chooseSortingAlgorythm()
            algorithm = Algorithm(x)
            
            if menu.askToRepeat():
                menu.cleanWindow()
            else:
                return 
