# Software Development Plan

## Phase 0: Requirements Analysis (tag name `analyzed`)
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
*   [ ] Explain the problem this program aims to solve.
    *   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.
*   [ ] List all of the data that is used by the program, making note of where it comes from.
    *   Explain what form the output will take.
*   [ ] List the algorithms that will be used (but don't write them yet).
*   [ ] Tag the last commit in this phase `analyzed`
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


### Instructions in my own words:

* I need to complete the classes that have been started. These classes include the card, the Deck, Menu, Menu Option, Rand Numbers, Tty colors, user interface, bingo and the run tests.
* The tty colors does not need to be changed.
* run Tests only needs to be modified if I want to change it, or if I complete the  project in a different way than the tests are expectin. I can also add any tests I want.
* part of the menu and the menu Option have been finished from what the c++ have implemented, but it is not finished yet.
* RandNumberSet has also been worked on by the C++ team, but there is a bug where some numbers will repeat. 
* a deck will have methods to print a specific bingo card from the deck, to print the entire deck to the screen, and to save the deck to a file supplied by the user.
* Cards will have their ID number printed, then it will print the name of each column BINGODARLYZEMPUX, columns will be seperated by | and rows will seperated with +-----+. Cards that are 
odd numbers will have a FREE! space in the middle. 
* Cards will be created and stored into memory but not printed out unless asked. 
* The user manual will tell people how to run the program, what menus are there, what responces are acceptable from the menu and how to create a deck and print out the cards, save them to 
a file, or exit the program. The user manual should also describe error messages the user might see and how to recover
* I also need to Draw a UML Class Diagram, This Must include each classess, how they relate to other classes, and what each class consists of.


### What this program aims to solve:

* This program will create a deck of bingo cards that follow the user's specifications. The user will choose the number of rowsXcolumns, and the range of numbers. Users will be able to 
print out specific cards or the entire deck. User will also be able to save a deck to a file they create. 

### Data used by the program and where it comes from:

* User will supply what the size of the card should be and the range of numbers found on the card this will come from the first menu. data created by this project will consist of the card 
ID
* The output will be in the form of text, The output my be printed by the user or saved in a file.

### Algorithms to be used:

* The functions to create and place all the random numbers is an algorithm that has *mostly* been created already.
* A small algorithm will be used to print all the cards.
* Another algorithm will be used to format the cards corectly.
* an algorithm will be used to ensure the numbers in each column are in the correct range.


## Phase 1: Design (tag name `designed`)
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [ ] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
*   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them later when testing
*   [ ] Tag the last commit in this phase `designed`
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*

### Function Signatures:

# Card Class:

* a card consists of its id and the RandNumSet.
* the card needs to be able to get the ID of any card. 
* it also needs to remember the size of the card (row X col)
* it also needs the col names.
* This class needs to be able to return the value of any row X col so it can be printed.
* the class needs to return the len of the card, this will be used for printing.
* This class also needs to be able to return the bingo card as a string

This class is called from the deck class when the user is creating a new deck.
The parameters will come from the UI.  

getID
return nID

numberAt(row, col)
key = grid[row][col]
assuming the grid is in a 2d list, we can find the value in the grid by iterating to the correct row and column

len
len1 = len(grid[0])
this will find the len of the first row which is the same as the col

str
For this function, I will iterate through the grid, and print them formatted
while I am iterating throught the grid, I will also print the boundry lines

print header '+' + '-' * 5 + '+'
	for row in grid:
		for cell in row
			print(f' {number} |' end = '')
		print()
print header again

# Deck Class

* the deck needs to know how many cards are in the deck, the card size, and the max number in the cards
* The deck needs to be able to return an int of how many cards are in the deck
* the deck needs to be able to return any card from the deck from it's ID
* the deck needs to be able to return all the cards from the deck

This class is called from the UI after the user gives the parameters for the deck.

len
return nNumCards

getItem(nIDx)
return cards[nIDx]

str
for card in cards
	card[card].str


# Menu class

* the menu needs to be colorful
* the menu will prompt the user for input, and repeat the prompt until it sees a recognized command
* the menu needs to check input to see if it is valid.
* it also needs to be able to return the number of menu options in the menu
* it has a function called getitem that will retrive an option by index, but I dont know what this is used for.
* this class also has a function called iadd which is used to append an option to the m arrOptionsm

**NOTE** The menu starts as an empty menu, all options are appended to it as needed.

iadd(option)
Options.append(option)

getitem(nIdx)
if 0 <= nIdx < len(self)
	return self.Options[nIdx]

len
return len(Options)

isValidCommand(chCommand)
for i in range(len(self))
	if Command.upper() == self[i].command.upper()
		return true
	return false

prompt
While True:
	options = []
	print header
	for i in range(len(self))
		option = self[i]
		if option is not None:
			print(option)
			opptions.append(self(option.getcommand))
	print(enter a command) (formatted)
	command = input()
	if self.isValidCommand(command)
		return command	
	else
		print this is not a valid option
		call prompt


# MenuOpiton Class

**NOTE** this class is used for presenting the options to the menu

* this class has a function called getCommand that will return a string, the command letter that activates an option
* this calss can also return a description of the menu Option
* It can also return the command letter and teh description

getCommand
return self.Command

getDescription
return self.description

str
return command + description


# RandNumberSet Class

* The min size is 3 and the max is 16!
* The minimum the numbers can be is the size X size, this is to ensure there are enough possible numbers so none are repeated
* This class will shuffle the numbers so they are always in a random order
* this class will return the next row of numbers because all numbers in a row need to be within a certain range.
* This class can return the segments
* it can also get the length of numbers aka the card size.
* It can return a specified row of bingo numbers

this class is called from the card class for filling in the cards with new numbers.
The parameters come from the UI

shuffle
for parts in segments
	random.shuffle(parts)
return parts

getNextRow
if RowPos >= nSize:
	return none
row = []
for seg in segments
	row.append(seg(nRowPos)
return row

getSegments
return arrSegments

str
strs =[]
for seg in segments
strs.append(str(seg))
return strs

len
return nSize

getitem
if 0 <= n < nSize:
row = []
for seg in segments
	row.append(seg[n])
return row
else
Index error


# User Interface Class

* this will present the user with the main menu and the deck menu. This can also validate input
* the first function is to run the class, which will present the user with their menu
* createDeck will create a new deck based on specifications from the user.
* this will aslo present the user with a deck menu
* getStr will return the input from the user
* getInt will return the input as an int from the user
* this class can also print a specific card from the deck to the users screen
* This class can also save the deck to any file
* this class needs to be able to print the entire deck to the user

**NOTE** input is case insensitive
The main menu allows the user to either create a new deck or exit the program
when the user selects create a new deck
the program will propmt the user for the size of the card
the maximum bingo number
the number of cards for the deck
**NOTE** when the menu is prompting the user for parameters of their deck, it should give minimum and maximum values

after all info is given, a new deck is created.

then a new menu appears, in this menu, the user can print a card to the screen, print all cards to the screen, save the entire deck to a file, or return to the menu

run
while true:
	print logo
	menu = menu(main)
	menu += menuOption(Create a new deck)
	+= exit
	command = menu.prompt()
	if command == c
		create deck
	elif == x
		break

createDeck
size = input("size of card")
maxNum = input(maxNum)
number = input(number of cards)
deckMenu()

deckMenu
either print a card, display the deck, save the deck, or return to the main menu
if printing a card
printCard
if printing entire deck
printDeck
if saving the deck
savedeck()

getStr
return user input

getInt
return user input

printCard
card[which card].str()

printDeck
deck.str()

saveDeck
filename = input(filename)
with open (filename, 'w') as f
	printDeck()



## Phase 2: Implementation (tag name `implemented`)
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan
*   [ ] Tag the last commit in this phase `implemented`


## Phase 3: Testing and Debugging (tag name `tested`)
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
*   [ ] Tag the last commit in this phase `tested`


## Phase 4: Deployment (tag name `deployed`)
*(5% of your effort)*

Deliver:

*   [ ] Tag the last commit in this phase `deployed`
*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.
