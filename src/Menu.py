
from TtyColors import TtyColors  	  	  


class Menu(TtyColors):  	  	  
    """  	  	  
    Present a Menu made of of MenuOptions to a user, and continue to prompt until they provide valid input  	  	  

    When the user's selection is alphabetic, it is matched without regard to case;  	  	  
    both upper- and lower-case letters are accepted  	  	  

    Inherit from class TtyColors to gain access to the color methods  	  	  
    """  	  	  

    def __init__(self, szHeader):  	  	  
        """  	  	  
        Create an empty Menu  	  	  

        Takes one string: the Menu's title  	  	  
        """  	  	  
        self.__m_szHeader = szHeader  	  	  
        self.__m_arrOptions = []  	  	  

    def __iadd__(self, option):  	  	  
        """  	  	  
        Append an option to __m_arrOptions  	  	  

        This method was called `operator+` in the C++ version  	  	  

        Be careful: No check is made for duplicate MenuOptions!  	  	  
        """  	  	  
        self.__m_arrOptions.append(option)  	  	  
        return self  	  	  

    def __getitem__(self, nIdx):  	  	  
        """  	  	  
        Retrieve an option by index  	  	  

        This method was called `operator[]` in the C++ version  	  	  
        """  	  	  
        if 0 <= nIdx < len(self):  	  	  
            return self.__m_arrOptions[nIdx]  	  	  
        else:  	  	  
            raise IndexError  	  	  

    def __len__(self):  	  	  
        """  	  	  
        Return an integer: the number of MenuOptions contained in this Menu  	  	  

        This method was called `length` in the C++ version, and was meant to be explicitly called  	  	  
        """  	  	  
        return len(self.__m_arrOptions)  	  	  

    def isValidCommand(self, chCommand):  	  	  
        """  	  	  
        Return a Boolean: whether a command is contained in our list of MenuOptions  	  	  

        Considers upper-case options the same as lower-case  	  	  
        """  	  	  
        for i in range(len(self)):  	  	  
            if chCommand.lower() == self[i].getCommand().lower():
                return True  	  	  
        return False  	  	  

    def prompt(self):  	  	  
        """  	  	  
        Return None: Display the menu and take a command from the user  	  	  

        The menu is repeated until the user provides a recognized command  	  	  
        """  	  	  
        while True:  	  	  
            options = []  	  	  
            header = f"{self.__m_szHeader} menu"  	  	  
            bar = "=" * len(header)  	  	  
            print(f"\n{bar}\n{self.white(header)}\n{bar}")  	  	  
            for i in range(len(self)):  	  	  
                option = self[i]  	  	  
                if option is not None:  	  	  
                    print(option)  	  	  
                    options.append(self.yellow(option.getCommand()))  	  	  

            print(self.white(f"\nEnter a {self.__m_szHeader} command"), f"({', '.join(options)})")  	  	  
            command = input()  	  	  
            if self.isValidCommand(command):  	  	  
                return command  	  	  
            else:  	  	  
                print(f"'{self.magenta(command.strip())}' is not a valid option")  	  	  
