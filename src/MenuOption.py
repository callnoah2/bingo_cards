
from TtyColors import TtyColors  	  	  


class MenuOption(TtyColors):  	  	  
    """  	  	  
    Represent an option in a text-based Menu  	  	  

    An option is a single letter paired with a description string  	  	  

    Inherit from class TtyColors to gain access to the color methods  	  	  
    """  	  	  

    def __init__(self, chCommand, szDescription):  	  	  
        """  	  	  
        Create a MenuOption  	  	  
        """  	  	  
        self.__m_chCommand = chCommand  	  	  
        if self.__m_chCommand == '':  	  	  
            self.__m_chCommand = '?'  	  	  
        elif len(self.__m_chCommand) > 1:  	  	  
            self.__m_chCommand = self.__m_chCommand[0]  	  	  

        self.__m_szDescription = szDescription  	  	  
        if self.__m_szDescription == '':  	  	  
            self.__m_szDescription = '???'  	  	  

    def getCommand(self):  	  	  
        """  	  	  
        Return a string: the command letter that activates this MenuOption  	  	  
        """  	  	  
        return self.__m_chCommand  	  	  

    def getDescription(self):  	  	  
        """  	  	  
        Return a string: the human-friendly description of this MenuOption  	  	  
        """  	  	  
        return self.__m_szDescription  	  	  

    def __str__(self):  	  	  
        """  	  	  
        Return a string: the command letter combined with its description  	  	  

        This is basically equivalent to the `operator<<` method in the C++ version  	  	  
        """  	  	  
        return f"{self.yellow(self.__m_chCommand)}) {self.cyan(self.__m_szDescription)}"  	  	  
