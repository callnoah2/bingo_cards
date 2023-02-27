# CS 1440 Assignment 4: Bingo!

*   [Instructions](./instructions/README.md)
    *   [Output examples](./instructions/examples/README.md)
    *   [Running Unit Tests](./instructions/Running_Unit_Tests.md)
    *   [How to Submit this Assignment](./instructions/How_To_Submit.md)
*   [Project Requirements](./instructions/Requirements.md)
*   C++ Team [Software Development Plan](./instructions/Cpp_Team_Plan.md)
*   C++ Team [UML Class Diagram](./instructions/Cpp_Team_UML.pdf)


*Note: this file is a placeholder for your notes.  When seeking help from TAs or tutors, replace this text with a description of your problem and push it to GitLab*


## Important!
**I have instructed the CS Coaches to _not_ help you write code for this assignment until you have completed the Design phase and tagged your repository `designed`.  Don't even think about writing code until you have carefully considered the design.  Countless software projects have gone awry because the design phase was neglected.  Don't become a statistic - think first, code after.**


## Get the starter code

*   Clone this repository and use it as a basis for your work.
    *   Run each of these commands one-at-a-time, without the `$` (that represents your shell's prompt).
    *   Replace `USERNAME` with your GitLab username, `LAST` and `FIRST` with your names as used on Canvas.

```bash
$ git clone git@gitlab.cs.usu.edu:erik.falor/cs1440-falor-erik-assn4 cs1440-assn4
$ cd cs1440-assn4
$ git remote rename origin old-origin
$ git remote add origin git@gitlab.cs.usu.edu:USERNAME/cs1440-LAST-FIRST-assn4.git
$ git push -u origin --all
```


## Overview

For your next project at DuckieCorp you are tasked with writing an interactive Bingo card generator.  This project was started by our C++ team, but partway through the customer and the project manager decided that Python would be a better platform for this system.  I translated the partially-completed C++ program into Python before the project was assigned to you.  Some traces of the original C++ coding style are still evident.

You will create a complete *programming product* consisting of

*   A clean program that can be easily modified
*   Documentation (both technical and user-oriented)
*   Unit Tests

As you well know, creating a *programming product* can take up to 3x as much time as just making a simple program.  Plan for this and carefully manage your time so that you can meet the deadline.


## Running the starter code

Unlike previous projects, this program uses an interactive menu and *does not* take command line arguments.

```
$ python src/bingo.py

     ########   ####  ##    ##   ######     #######   ####
     ##     ##   ##   ###   ##  ##    ##   ##     ##  ####
     ##     ##   ##   ####  ##  ##         ##     ##  ####
     ########    ##   ## ## ##  ##   ####  ##     ##   ##
     ##     ##   ##   ##  ####  ##    ##   ##     ##
     ##     ##   ##   ##   ###  ##    ##   ##     ##  ####
     ########   ####  ##    ##   ######     #######   ####
                                         by DuckieCorp(tm)

=========
Main menu
=========
C) Create a new deck
X) Exit the program

Enter a Main command (C, X)
c
TODO: Walk the user through the process of creating a new Deck of Cards
  * prompt for the size of card
  * prompt for the maximum Bingo number to use on each card
  * prompt for the number of cards in the deck
TODO: create the new Deck object

=========
Deck menu
=========
P) Print a card to the screen
D) Display the whole deck to the screen
S) Save the whole deck to a file
X) Return to the Main menu

Enter a Deck command (P, D, S, X)
```

Additionally, menus are **case-insensitive**; both `x` and `X` will make the program exit.


## Running Unit Tests

The starter code consists of 16 test cases, 9 of which already pass.  You will increase the number of passing tests as you progress in the project.

*   You may run the unit tests through PyCharm or the shell.
*   To run the tests from your shell, run `src/runTests.py`.  This command will produce a lot of output:

```
$ python src/runTests.py
test_add_options (Testing.testMenu.TestMenu)
Ensure that options can be added to a Menu ... ok
test_get_options (Testing.testMenu.TestMenu)
Ensure that menu options can be retrieved from Menus ... ok
test_is_valid_command (Testing.testMenu.TestMenu)
Ensure Menu can distinguish bad commands from the good ones ... ok

... dozens of lines snipped ...

======================================================================
FAIL: test_len (Testing.testDeck.TestDeck)
Ensure that Decks contain the expected number of cards
----------------------------------------------------------------------
Traceback (most recent call last):
  File "src/Testing/testDeck.py", line 36, in setUp
    self.assertTrue(False, "TODO: implement this test")
AssertionError: False is not true : TODO: implement this test

----------------------------------------------------------------------
Ran 16 tests in 0.018s

FAILED (failures=7)
```

Full instructions are found in [Running Unit Tests](./instructions/Running_Unit_Tests.md).
