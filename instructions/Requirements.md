# CS 1440 Assignment 4: Bingo! - Project Requirements

In this project you will design classes that work together to generate a deck of Bingo cards.

Bingo is a simple game where players try to mark all numbers in a row or column or along one of the two diagonals of a Bingo card. The rules of the game are actually not important for this project, as you are only making a program to print the cards.

This program is only partly complete: the finished program will allow a user to create a deck, print a card from the current deck, display the entire deck, or save the entire deck as a text file.  Unit tests are provided, though at this early stage many will fail because the program is still incomplete.

*   [User Interface](#user-interface)
*   [Bingo Cards](#bingo-cards)
*   [RandomNumberSet](#randomnumberset)
*   [Decks of Bingo Cards](#decks-of-bingo-cards)
*   [Format of Cards](#format-of-cards)
*   [Test-Driven Development](#test-driven-development)
*   [Writing the User Manual](#writing-the-user-manual)
*   [Drawing UML Class Diagrams](#drawing-uml-class-diagrams)


## User Interface

0.  DuckieCorp's C++ team completed the `Menu` and `MenuOption` classes before the project was turned over to you
    *   They designed the `UserInterface` class and implemented only those parts they needed
    *   You will notice some bits of C++ style showing through, especially in the names of variables and methods
    *   This naming style is called [Hungarian Notation](https://en.wikipedia.org/wiki/Hungarian_notation)
    *   You can change these if you don't like them, but be careful that you don't add new bugs into otherwise working code!
1.  C++ enforces the privacy of methods and data members within classes
    *   Python has privacy, too, but it's not nearly as strict as languages like C++ and Java
    *   Python variables and methods whose names begin with double underscores `__` are *private*
        *   *Example:* in `src/MenuOption.py` the attribute `__m_chCommand` is private, as it starts with `__`, but the method `getCommand()` is public.
        *   This **does not** apply to "dunders", identifiers that both *begin* and *end* with underscores - **dunders are always public**
        *   It is easy to learn how to defeat these safeguards by inspecting classes in the REPL
        *   Don't take advantage of this and write code that undermines privacy
2.  Follow these general UI principles in this project:
    *   Case doesn't matter; *upper* case is just as valid as *lower* case
    *   You **do not** need to validate file names entered by the user; if the user enters a bad file name, your program should crash with Python's default error message
3.  This program displays menus and prompts the user for input instead of getting arguments from `sys.argv`
    *   Menu options are **case-insensitive**
        *   Note that the starter code displays *upper* case letters for its menus, even though it also accepts *lower* case input!
        *   For consistency's sake, keep to this convention
    *   Prompts are repeated until the user provides valid input
        *   For *string* input, "valid" means that the user typed something, and didn't just hit **Enter**
        *   For *integer* input, "valid" means that the user's input passes the `.isdigit()` test **and** lies within the accepted range
            *   Prompts asking for numeric input *must* display the acceptable range of numbers
    *   Display helpful and appropriate messages to remind the user what kind of input is expected
    *   Continue to redisplay the prompt until valid data is provided
        *   Do not return to the previous menu or exit the program when invalid data is given
        *   Take special care that your program does not get into a bad state when bad data is input by the user; your program should be **robust**



## Bingo Cards

0.  Every Card has a unique integer identifier
    *   This number can be the same as its position within its Deck
1.  A Bingo Card is an $N x N$ grid, where $N$ is the size of the Card
    *   The typical size is 5x5, but we'll allow Cards to vary in size from 3x3 to 16x16.
2.  Numbers on Cards are drawn from the set of integers $[ 1 \ldots M ]$ (inclusive)
    *   $M$ is the maximum number that may appear in a Deck, its value depends on the size of the Card
    *   $M$ is chosen by the user from the range $[ 2 * N^2 \ldots floor(3.9 * N^2) ]$ (inclusive).
    *   A Bingo number *cannot* appear on the same Card more than once
    *   A Bingo number *can* appear on multiple Cards in the same Deck
3.  The columns on a traditional 5x5 Bingo Card are named `B`, `I`, `N`, `G`, and `O`
    *   This naming scheme has been extended to accommodate Cards with up to 16 columns such that each column has a unique name
    *   Numbers in each column are drawn from $N$ non-overlapping subsets of $[ 1 \ldots M ]$, with values increasing column-wise from left to right
        *   On a 5x5 Card, numbers in column `B` are drawn from the first $\frac{1}{5}$th of numbers starting from `1`, column `I` gets the next $\frac{1}{5}$th of numbers, and so on
        *   For a 3x3 Card, numbers in column `B` are drawn from the first $\frac{1}{3}$rd of numbers, column `I` gets the next $\frac{1}{3}$rd of numbers, and column `N` gets the last $\frac{1}{3}$rd
        *   This requirement was already fulfilled by the C++ team in the `RandNumberSet` class
        *   However, one of the unit tests indicates that `RandNumberSet` produces duplicate numbers.  **You need to fix this bug.**
4.  Odd-sized Cards have a **FREE!** square in the center
    *   **FREE!** squares contain the string `"FREE!"` instead of a number
    *   Even-sized Cards don't have a center square and, thus, no **FREE!** square
5.  Once generated, a Card's appearance does not change
    *   If a Card is displayed multiple times, its appearance is identical each time



## RandNumberSet

0.  This class was translated straight across from a C++ implementation, along with the Unit Tests
    *   One of the Unit Tests is failing, indicating that there is still a bug in the code
    *   Find and fix this bug
    *   Apart from this bug, you can consider this code to be complete and correct
1.  This class exists to help create Cards that meet the requirements listed above
2.  A Card will *use* a `RandNumberSet` object while it is being created
    *   A Card consists of rows of numbers, and the `RandNumberSet` is designed to give out one row of numbers at a time
3.  A Card *does not* need to keep its `RandNumberSet` after the constructor is finished
4.  Your program *does not* need to make new `RandNumberSet`s for each Card that is created
    *   `RandNumberSet` has a method called `shuffle()` which resets it



## Decks of Bingo Cards

0.  The number of Bingo Cards in a Deck is chosen by the user from the range $[ 2 \ldots 8192 ]$ (inclusive).
1.  The `Deck` class must have the following capabilities:
    -   A method to print a specific Card in the Deck to the screen
    -   A method to print whole Deck to the screen
    -   A method to save a Deck to a file named by the user
        -   Read the documentation for `print()` to learn how to print text into a file opened in **write mode**
        -   Read the documentation for `open()` to learn how to open a file in **write mode**
        -   `open()` can take more than one parameter
            -   The one you are looking for is an optional *string* parameter that can truncate a file
        -   The only validation to do on the user's file name is to reject empty strings
            -   It is not your responsibility to validate that file name entered by the user is legal; this varies by operating system, and is a huge headache
            -   Just let `open()` raise an exception when the user gives a bad file name
            -   In Python, files that don't exist are automatically created and existing files are overwritten when `open()` is called in write mode; you do not need to look to see if a file already exists before writing to it
            -   Accept the user's proposed file name as is; do not add directories or file name extensions to the string
        -   When you're done writing the Deck to a file, don't forget to `.close()` it!
2.  When printing all a Deck's Cards to the screen or to a file, simply print every Card, one after the other
3.  If you don't change the method definitions already provided for you in `Deck.py`, you should not have to change `UserInterface.py`
    *   You may add new methods and attributes to `Deck.py` as you see fit
4.  Your solution may contain other classes besides those given in the starter code
5.  The Deck should be able to retrieve a Card given the identifier, so the user can print just that Card to the screen
    *   After a Deck has been created, a Card that is displayed multiple times appears identical each time
6.  When a new Deck is created the previous Deck is lost
7.  The program *must not* construct any Cards if the user-supplied Card size, number of Cards, or maximum of Bingo numbers is invalid



## Format of Cards

0.  The Card's ID number is printed first
1.  The name of each column is centered above its cell
    *   Each column is named by a unique letter
    *   You can use these letters `BINGODARLYZEMPUX`
    *   The Python format specification for centered text is `:^N`, where `N` is the width of the field in which to place the text
        *   Using an f-string, The number `123` is centered in a field of 12 columns between `|` chars like this:
            ```python
            f"|{123:^12}|"
            ```
        *   Idem., but using `str.format()`:
            ```python
            "|{:^12}|".format(123)
            ```
        *   [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#formatspec) official documentation
2.  Columns are separated by pipe characters `|`
3.  Rows are bounded by a line of the form `+-----+-----+` that is as wide as the entire Card
    *   There is one boundary line at the top and bottom of every Card
4.  Cell contents are centered in a field 5 characters wide
    *   The widest value that can appear in a Card is the string `"FREE!"`
5.  The format of the Cards is always the same, regardless of whether they are printed to the screen or written to a file
    *   The menus use the methods defined in the `TtyColors` class to add a splash of color
        *   You **do not** need to apply colors to the Bingo Cards
        *   If you want to make your Bingo Cards colorful, *don't add color* when **saving your Deck to a file**
        *   They will look fine when you `cat` the file, but will be full of funny escape characters when you open the file in an editor!

When a Card is printed to the screen or to a file, it should be formatted *exactly* like these specimens:

**Odd-sized Card**

```
Card #62
   B     I     N     G     O
+-----+-----+-----+-----+-----+
| 10  | 17  | 35  | 50  | 64  |
+-----+-----+-----+-----+-----+
| 15  | 19  | 44  | 56  | 70  |
+-----+-----+-----+-----+-----+
|  8  | 30  |FREE!| 55  | 63  |
+-----+-----+-----+-----+-----+
| 11  | 26  | 32  | 59  | 67  |
+-----+-----+-----+-----+-----+
|  1  | 23  | 45  | 52  | 62  |
+-----+-----+-----+-----+-----+
```

**Even-sized Card:**

```
Card #10
   B     I     N     G
+-----+-----+-----+-----+
|  8  | 16  | 20  | 27  |
+-----+-----+-----+-----+
|  1  |  9  | 22  | 31  |
+-----+-----+-----+-----+
|  3  | 13  | 19  | 29  |
+-----+-----+-----+-----+
|  7  | 14  | 24  | 26  |
+-----+-----+-----+-----+
```

Examples of every size of Card are found in the [examples](./examples/) directory.

Here is some documentation that you may find helpful:

*   [Custom String Formatting](https://docs.python.org/3/library/string.html#custom-string-formatting)
*   [Format examples](https://docs.python.org/3/library/string.html#formatexamples)
*   [PEP 3101](https://peps.python.org/pep-3101/)
*   Run `help("FORMATTING")` in the REPL



## Test-Driven Development

An important part of this assignment is to learn about unit tests and to gain experience approaching a problem through the Test-Driven Development methodology.  Writing your program to comply with the provided unit tests is meant to guide you toward a correct and robust solution, and is worth a large proportion of the points on this assignment.

However, you are given latitude in how your solution is structured and are free to add, remove, or refactor classes to meet the design you crafted in UML.  It is not intended for you to take advantage of this latitude in order to avoid unit tests.

*   16 unit tests are provided in the starter code.  All tests must pass in the final submission
    *   2 tests have been identified by the C++ team for the `Deck` class
    *   4 tests have been identified by the C++ team for the `Card` class
    *   You will complete these tests by the end of the Testing phase


As you craft your solution, please keep these guidelines in mind:

*   The unit tests that are already provided make some assumptions about the way your code works
    *   My assumptions should not be seen as a "hint" to guide you to the "right way" of writing this program
    *   If your code does not fit my tests, change the tests to match your implementation
        *   If a unit test fails because you renamed a class, method or data member, update the unit test accordingly
        *   If a unit test fails because you removed a class, method or data member, from your design, you must _replace_ that unit test with another non-trivial unit test
        *   If a unit test fails because you moved a piece of functionality from one class to another, move that unit test into the file corresponding to the new class
*   Do not create _trivial_ unit tests
    *   A trivial unit test unconditionally passes, and does not give any insight about your code
*   Do not delete unit tests just because they don't pass; find ways to make your code compatible with the unit test, or re-write the test
*   Do not change unit tests to become less strict or trivial; instead, figure out how to make your code more robust
*   Some of the unit tests can take a *really* long time to run
    *   If you can, seek to improve the performance of your code so that `src/runTests.py` can finish in less than one minute
    *   If you can't make the test run in under a minute, adjust the test parameters downward so the test is less thorough, but still comprehensive

_**TL;DR**_ You have been given 16 non-trivial unit tests.  Your final submission must contain _at least_ 16 non-trivial unit tests that all pass.



## Writing the User Manual

The User Manual describes only the user interface of the program.  The target audience for the manual is somebody with a little familiarity with computers and no knowledge of the Python programming language.

The manual should answer such questions as:

0.  How to run the program
1.  What menus will the user see
2.  What responses should the user give in response to those menus
3.  How to perform the basic operations of the program (in our case, how to create a Deck, how to print Cards in the Deck, how to save a Deck to a file, how to quit the program)
4.  What error messages the user may expect, and how to recover from mistakes

The User Manual differs from the Software Development Plan in that it *should not* include details about *how* the program works.  The manual *should not* describe the algorithms and data structures the program uses.


### Instructions that you do not need to write

You may assume that your user already knows how to

0.  Install the program onto their computer
1.  Open a terminal and navigate to the project directory



## Drawing UML Class Diagrams

You may draw your UML class diagram any way you prefer, so long as they are *clean*, *legible* and *correct*.

*   *Clean*
    *   Straight lines
    *   Sharp corners
    *   All lines of boxes connect
    *   Text runs in parallel lines
*   *Legible*
    *   Text is easy to read
    *   Neutral colors that don't distract
    *   Minimize the number of crossed lines
*   *Correct*
    *   Your diagram is a UML Class Diagram instead of another type of diagram
    *   Only valid UML Class Diagram elements are used
        *   You only need use the elements shown in the lecture notes; no more, no less!

You can draw your class diagrams by hand, but if you do that they need to look *really* good.


### Drawing UML Class Diagrams in Diagrams.net

[Diagrams.net](https://app.diagrams.net/) is a simple web app for making diagrams.  It is free, easy to use, and good enough for this project.

0.  Open the website
1.  Click "Create New Diagram"
2.  Select the "Basic" "Blank Diagram"
    *   Don't use one of the pre-defined UML templates, as they start with a bunch of placeholder junk that you'll just end up deleting
3.  Find the UML section in the accordion list on the left-hand side of the screen
    *   There are multiple shapes available with names like `Class`, `Class 2`, `Class 5`, etc.
    *   Make sure that the classes appearing on your diagram have 3 sections as described in our lectures:
    *   ```mermaid
        classDiagram
        direction LR
        class Classic {
            +field0 : type0
            +field1 : type1
            +method0() type0
            +method1() type1
        }
        ```
4.  Download your diagram as a PDF by clicking **File** -> **Export**.
    *   **Do not select _Transparent Background_**
5.  Click **Download** to create the PDF.  Depending on your browser, you may be redirected to a new tab from which you will need to save the file.
