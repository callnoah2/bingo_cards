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
