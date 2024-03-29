from NumberPicker import NumberPicker
from Deck import Deck
from Menu import Menu
from MenuOption import MenuOption
from TtyColors import TtyColors
from RandNumberSet import RandNumberSet

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
        valid_inputs = [x.lower() for x in valid_inputs]  # convert valid_inputs to lowercase
        while True:
            response = input(prompt).lower()
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
            command = str(menu.prompt())
            if command in ["c","C"]:
                self.__createDeck()
            elif command in ["x", "X"]:
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

    def __createDeck(self):

        # Prompt for the size of card
        nCardSize = self.__getInt("Please Enter the Size of the Card in range [3 - 16]: ", 3, 16)

        # Prompt for the maximum Bingo number to use on each card
        minNum = 2 * nCardSize ** 2
        maxNum = int(3.9 * nCardSize ** 2)
        nMaxNum = self.__getInt(f"Please Enter the max Bingo number(min: {minNum} - max: {maxNum}): ", minNum, maxNum)

        # Prompt for the number of cards in the deck
        maxnumCards = 8192
        nNumCards = self.__getInt(f"Please enter the number of Cards to be created (max: {maxnumCards}): ", 1, maxnumCards)

        # Create a new Deck object with the user input values
        rand_num_set = RandNumberSet(nCardSize, nMaxNum)
        deck = Deck(nCardSize, nNumCards, nMaxNum, rand_num_set)

        # Set the deck attribute of the UserInterface object to the newly created deck
        self.__m_deck = deck

        # Present the deck menu to the user
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

    def gameMenu(self):
        while True:
            menu = Menu("Game")
            menu += MenuOption("N", "Generate a number")
            menu += MenuOption("X", "Return to deck menu")
            command = str(menu.prompt().lower())
            if command in ["n", "N"]:
                self.__pickNum()
                if self.winCheck() == True:
                    break
            elif command in ["x", "X"]:
                break

    def __deckMenu(self, nNumCards, nCardSize):
        """
        Return None

        Present the deck menu to user until a valid selection is chosen
        """
        while True:
            menu = Menu("Deck")
            menu += MenuOption("P", "Print a card to the screen")
            menu += MenuOption("D", "Display the whole deck to the screen")
            menu += MenuOption("S", "Save the deck")
            menu += MenuOption("G", "Play BINGO!")
            menu += MenuOption("X", "Return to main menu")
            command = str(menu.prompt().lower())
            if command in ["p", "P"]:
                self.__printCard(nNumCards, nCardSize)
            elif command in ["d", "D"]:
                self.__printDeck()
            elif command in ["s", "S"]:
                self.__saveDeck()
            elif command in ["g", "G"]:
                self.gameMenu()
            elif command in ["x", "X"]:
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
        while True:
            filename = input("Enter the filename to save the deck: ")
            if not filename:
                print("Invalid filename!")
                continue
            try:
                with open(filename, "w") as file:
                    for card in self.__m_deck:
                        file.write(str(card))
                        file.write("\n\n")
                print(f"Deck saved to {filename}!")
                return
            except OSError:
                print("Error saving deck!")
