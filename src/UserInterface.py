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

from Deck import Deck
from Menu import Menu
from MenuOption import MenuOption
from TtyColors import TtyColors

class UserInterface(TtyColors):
    """  	  	  
    Provide the UserInterface for the program, which consists of the Main menu and the Deck menu  	  	  

    Also provides methods for accepting and validating user input  	  	  

    Inherit from class TtyColors to gain access to the color methods  	  	  
    """

    def __init__(self):
        self.__m_deck = None


    def __getStr(self, prompt, valid_inputs):
        """
        Return a string input from the user that is contained in valid_inputs, prompted by string prompt.
        """
        while True:
            response = input(prompt).strip().lower()
            if response in valid_inputs:
                return response
            print(f"Invalid input! Please enter one of the following: {', '.join(valid_inputs)}")

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
            # command = self.__getStr(menu.prompt(), ["c", "x"])
            command = str(menu.prompt())
            if command == "c":
                self.__createDeck()
            elif command == "x":
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

        # Prompt for the size of card
        nCardSize = self.__getInt("Please Enter the Size of the Card in range [3 - 16]: ", 3, 16)

        # Prompt for the maximum Bingo number to use on each card
        minNum = 2 * nCardSize ** 2
        maxNum = (3.9 * nCardSize ** 2) // 1
        nMaxNum = self.__getInt(f"Please Enter the max Bingo number(min: {minNum} - max: {maxNum}): ", minNum, maxNum)

        # Prompt for the number of cards in the deck
        nNumCards = self.__getInt("Please enter the number of Cards to be created: ", 1, float("inf"))

        # Create a new Deck object with the user input values
        self.__m_deck = Deck(nCardSize, nNumCards, nMaxNum)
        self.__deckMenu(nNumCards, nCardSize)

    def __getInt(self, prompt, lo, hi):
        """
        Return an integer value between lo and hi inclusive, prompted by string prompt.
        """
        while True:
            try:
                num = int(input(prompt))
                if lo <= num <= hi:
                    return num
            except ValueError:
                pass
            print(f"Invalid input! Please enter an integer between {lo} and {hi}.")

    def __deckMenu(self, nNumCards, nCardSize):
        """
        Return None

        Present the deck menu to user until a valid selection is chosen
        """
        while True:
            menu = Menu("Deck")
            menu += MenuOption("P", "Print a card to the screen")
            menu += MenuOption("D", "Display the whole deck to the screen")
            menu += MenuOption("S", "Shuffle the deck")
            menu += MenuOption("X", "Return to main menu")
            command = str(menu.prompt())
            if command == "p":
                self.__printCard(nNumCards, nCardSize)
            elif command == "d":
                self.__printDeck()
            elif command == "s":
                self.__saveDeck()
            elif command == "x":
                break

    def __printDeck(self):
        """
           Print the entire deck of cards to the screen.
           """
        if not self.__m_deck:
            print(self.red("No deck has been created yet."))
        else:
            for i, card in enumerate(self.__m_deck):
                print(card)

    def __printCard(self, nNumCards, nCardSize):
        """
           Print a single card from the deck to the console
           """
        if self.__m_deck is None:
            print("No deck created yet.")
            return

        card_number = self.__getInt(f"Enter the card number to print (1-{nNumCards}): ", 1, nNumCards)

        # The deck is 0-indexed, so we need to subtract 1 from the card number to get the correct index
        card_index = card_number - 1
        card = self.__m_deck[card_index]
        print(card)

    def __saveDeck(self):
        """  	  	  
        Return None: Save a Deck to a file  	  	  

        Prompt user for the name of file to write the entire Deck into  	  	  
        """
        fileName = input("Please enter a filename: ")

        raise NotImplementedError("TODO: Save a Deck to a file")
