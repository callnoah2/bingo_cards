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

from math import floor  	  	  

from Deck import Deck
from Menu import Menu  	  	  
from MenuOption import MenuOption  	  	  
from TtyColors import TtyColors
from Card import Card


class UserInterface(TtyColors):  	  	  
    """  	  	  
    Provide the UserInterface for the program, which consists of the Main menu and the Deck menu  	  	  

    Also provides methods for accepting and validating user input  	  	  

    Inherit from class TtyColors to gain access to the color methods  	  	  
    """  	  	  

    def __init__(self):  	  	  
        self.__m_deck = None  	  	  

    def run(self):  	  	  
        """  	  	  
        Return None: present the main menu to the user  	  	  

        Repeatedly prompt for a valid command until good input is given, or the program is exited  	  	  
        """  	  	  
        while True:  	  	  
            self.__logo()  	  	  
            menu = Menu("Main")  	  	  
            menu += MenuOption("C", "Create a new deck")  	  	  
            menu += MenuOption("X", "Exit the program")  	  	  
            command = menu.prompt()  	  	  
            if command.upper() == "C":  	  	  
                self.__createDeck()  	  	  
            elif command.upper() == "X":  	  	  
                break  	  	  

    def __logo(self):  	  	  
        print()  	  	  
        print(self.green("     ######## "), self.magenta("  ####"), self.blue("  ##    ##"), self.yellow("   ######  "), self.red("   ####### "), self.cyan("  ####"), sep="")  	  	  
        print(self.green("     ##     ##"), self.magenta("   ## "), self.blue("  ###   ##"), self.yellow("  ##    ## "), self.red("  ##     ##"), self.cyan("  ####"), sep="")  	  	  
        print(self.green("     ##     ##"), self.magenta("   ## "), self.blue("  ####  ##"), self.yellow("  ##       "), self.red("  ##     ##"), self.cyan("  ####"), sep="")  	  	  
        print(self.green("     ######## "), self.magenta("   ## "), self.blue("  ## ## ##"), self.yellow("  ##   ####"), self.red("  ##     ##"), self.cyan("   ##"), sep="")  	  	  
        print(self.green("     ##     ##"), self.magenta("   ## "), self.blue("  ##  ####"), self.yellow("  ##    ## "), self.red("  ##     ##"), sep="")  	  	  
        print(self.green("     ##     ##"), self.magenta("   ## "), self.blue("  ##   ###"), self.yellow("  ##    ## "), self.red("  ##     ##"), self.cyan("  ####"), sep="")  	  	  
        print(self.green("     ######## "), self.magenta("  ####"), self.blue("  ##    ##"), self.yellow("   ######  "), self.red("   ####### "), self.cyan("  ####"), sep="")  	  	  
        print("                                         by ", self.yellow("DuckieCorp"), "(tm)", sep="")  	  	  

    def __createDeck(self):  	  	  
        """  	  	  
        Return None: Create a new Deck  	  	  

        The Deck is stored in self.__m_deck  	  	  
        """  	  	  
        print("TODO: Walk the user through these prompts in this order:")  	  	  
        print("TODO:  * prompt for the size of card")
        Dimentions = int(input("Please Enter the Size of the Card: "))
        print("TODO:  * prompt for the maximum Bingo number to use on each card")
        MaxNum = int(input("Please Enter the max Bingo number(min:): "))
        print("TODO:  * prompt for the number of cards in the deck")
        numCard = int(input("Please enter the number of Cards to be created: "))
        print("TODO: create the new Deck object")  	  	  
        self.__deckMenu()

    def __deckMenu(self):
        """  	  	  
        Return None  	  	  

        Present the deck menu to user until a valid selection is chosen  	  	  
        """  	  	  
        menu = Menu("Deck")  	  	  
        menu += MenuOption("P", "Print a card to the screen")  	  	  
        menu += MenuOption("D", "Display the whole deck to the screen")  	  	  
        menu += MenuOption("S", "Save the whole deck to a file")  	  	  
        menu += MenuOption("X", "Return to the Main menu")  	  	  

        while True:  	  	  
            command = menu.prompt()  	  	  
            if command.upper() == "P":  	  	  
                self.__printCard()  	  	  
            elif command.upper() == "D":  	  	  
                print("TODO: Print the Deck to the screen")  	  	  
                print(self.__m_deck)  	  	  
            elif command.upper() == "S":  	  	  
                self.__saveDeck()  	  	  
            elif command.upper() == "X":  	  	  
                break  	  	  

    def __getStr(self, prompt):  	  	  
        """  	  	  
        Return a string: non-empty input entered by the user  	  	  

        Take a prompt string as input  	  	  
        Repeat the prompt until a non-empty string is provided  	  	  
        """  	  	  
        raise NotImplementedError("TODO: Return a non-empty string entered by the user")  	  	  


    def __getInt(self, prompt, lo, hi):  	  	  
        """  	  	  
        Return an integer: validated integer input by user  	  	  

        Take a prompt string, low and high integers as input  	  	  
        Repeat the prompt until an integer that is in-range is provided  	  	  
        """  	  	  
        raise NotImplementedError("TODO: Return a validated integer input by user")  	  	  

    def __printDeck(self):
        Deck.__str__()

    def __printCard(self):
        """  	  	  
        Return None: Print one Card from the Deck  	  	  

        Prompt user for a Card ID  	  	  
        """
        printCard = int(input("Which Card: "))
        Card.__str__(Card[printCard])
        raise NotImplementedError("TODO: Print one Card from the Deck")

    def __saveDeck(self):  	  	  
        """  	  	  
        Return None: Save a Deck to a file  	  	  

        Prompt user for the name of file to write the entire Deck into  	  	  
        """
        fileName = input("Please enter a filename: ")

        raise NotImplementedError("TODO: Save a Deck to a file")  	  	  
