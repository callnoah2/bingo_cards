#                         ,  	  	  
#                        (o)<  DuckieCorp Software License  	  	  
#                   .____//  	  	  
#                    \ <' )   Copyright (c) 2023 Erik Falor  	  	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	  	  
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION  	  	  
#  	  	  
# You may reproduce and distribute copies of the Work in any medium,  	  	  
# with or without modifications, provided that You meet the following  	  	  
# conditions:  	  	  
#  	  	  
#   (a) You must give any other recipients of the Work a copy of this  	  	  
#       License; and  	  	  
#   (b) You must cause any modified files to carry prominent notices  	  	  
#       stating that You changed the files; and  	  	  
#   (c) You must retain, in the Source form of the files that You  	  	  
#       distribute, all copyright, patent, trademark, and attribution  	  	  
#       notices from the Source form of the Work; and  	  	  
#   (d) You do not misuse the trade names, trademarks, service marks,  	  	  
#       or product names of the Licensor, except as required for  	  	  
#       reasonable and customary use of the source files.  	  	  

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
