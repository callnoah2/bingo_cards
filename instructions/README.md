# CS 1440 Assignment 4: Bingo! - Instructions

## Previous Semester Assignment Statistics

Statistic                        | Value
--------------------------------:|:---------------
Average Hours Spent              | 11.49
Standard Deviation Hours         | 5.698
Average Score % (Grade)          | 85.5% (B)
% students thought this was Easy | 17.7%
... Medium                       | 54.2%
... Hard                         | 15.6%
... Too Hard/Did not complete    | 10.4%


**Important!**

**I have instructed the CS Coaches to _not_ help you write code for this assignment until you have completed the Design phase and tagged your repository `designed`.  Don't even think about writing code until you have carefully considered the design.  Countless software projects have gone awry because the design phase was neglected.  Don't become a statistic - think first, code later.**


*   [How to Do This Assignment](#how-to-do-this-assignment)
    *   [Phase 0: Requirements Analysis](#phase-0-requirements-analysis-tag-name-analyzed)
    *   [Phase 1: Design](#phase-1-design-tag-name-designed)
    *   [Phase 2: Implementation](#phase-2-implementation-tag-name-implemented)
    *   [Phase 3: Testing and Debugging](#phase-3-testing-and-debugging-tag-name-tested)
    *   [Phase 4: Deployment](#phase-4-deployment-tag-name-deployed)
    *   [Phase 5: Maintenance](#phase-5-maintenance)
*   [What We Look for When Grading](#what-we-look-for-when-grading)
*   [Important Things to Watch Out For](#important-things-to-watch-out-for)


## How to Do This Assignment

*   Your grade on this assignment depends upon how well you follow the SDP.  You demonstrate this by following instructions, writing clear documentation, and by *tagging* commits.
    *   Incorrectly spelled/capitalized tags are ignored.
    *   **If you tag the wrong commit**, or **incorrectly spell a tag** refer to `Using_Git/Intermediate_Git.md` in the lecture notes for instructions.


### Phase 0: Requirements Analysis (tag name `analyzed`)
*(20% of your effort)*

**Important - do not change any code in this phase**

0.  Read the [Project Requirements](./Requirements.md) to orient yourself with the project.
    *   Study the [SDP](./Cpp_Team_Plan.md) and [UML class diagram](./Cpp_Team_UML.pdf) written by the DuckieCorp C++ team
    *   Read and run the starter code to learn what they have already accomplished.
    *   Run the unit tests provided with the code, and note which tests pass and fail
    *   See [Running Unit Tests.md](./Running_Unit_Tests.md) for instructions on running the tests.
1.  Take the **Starter Code Quiz** on Canvas.
    *   Do not worry if you can't answer all of the questions yet
    *   You can re-take the quiz as many times as you want before the assignment is due
2.  Fill out **Phase 0** in Plan.md; explain in your *own words* what the program does, how it does it, and what changes you expect to make.
3.  Track your time in Signature.md.
4.  **Tag** the last commit in this phase `analyzed`
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


### Phase 1: Design (tag name `designed`)
*(30% of your effort)*

**Important - Unit Tests are the only Python code that is committed in this phase**

0.  You should be able to get 100% on the **Starter Code Quiz** by the end of this phase.
1.  Review the **UML Class Diagram** and **Software Development Plan** created by the C++ team
    *   C++ Team [UML Class Diagram](./Cpp_Team_UML.pdf)
    *   C++ Team [Software Development Plan](./Cpp_Team_Plan.md)
    *   Write between **250-300 words** of remarks in `doc/Reviews.md`, answering these questions:
        *   What are your overall impressions about the C++ team's design?
        *   What did you learn from the C++ team's UML Class Diagram?
        *   Did the class diagram help you understand/navigate the source code?
        *   What did you learn from the C++ team's Software Development Plan?
2.  Redraw the C++ team's **UML class diagram** using a drawing tool of your choice
    *   If you don't have a preference, use [Diagrams.net](https://diagrams.net).  Detailed instructions are [here](Requirements.md#drawing-uml-class-diagrams-in-diagrams-net)
    *   Translate C++ names to their Python equivalents
        *   `length()` and `size()` become `__len__()` in Python
        *   `operator[]()` becomes `__getitem__()`
        *   `operator<<()` is equivalent to `__str__()`
        *   The `void` type in C++ is equivalent to Python's `None` (technically `None` is a value of type `NoneType`; because `None` is the *only* value of `NoneType` you may use them interchangeably).
    *   You may rename other methods and variables; if you do, update the source code as well!
    *   You are not limited to using only what is provided in the starter code
        *   You may devise new classes, methods and data members to satisfy the customer's requirements; include these new components on this draft
        *   You may also remove elements from the starter code; that's fine as long as it is **documented** in your plan
    *   Do not include `bingo.py` on this diagram - it does not define any classes
    *   Do not include any files related to Unit Tests
        *   If "test" appears in the file's name, leave it out
    *   Save your diagram as `doc/UML.pdf`
3.  Design new methods on paper; **don't rewrite the files in src/ yet**.
    *   In this phase sketch out your *pseudocode*.
    *   Do not paste Python code into Plan.md; when we want to see your code we will read the `.py` files.
    *   Walk through the pseudocode in your head, with a pad of paper or a whiteboard to convince yourself that your design will work.
    *   You may write *some* runnable Python code to test out your ideas.  This is called *prototyping*, and is a normal part of the design process.
    *   Do not become too attached to your prototype!  Be prepared to delete prototype code after this phase.  It helps to *not* write prototype code in the same files as *real* code.
4.  Write the first draft of **unit tests** for the `Card` and `Deck` classes
    *   Practice *Test-Driven Development*: at this point in the project these tests will not pass because they code they test hasn't yet been written.
    *   These tests are a design tool that help you plan what these classes will do.
    *   Follow the notes left by the C++ team in Phase 3 of their software plan.
    *   See [Running Unit Tests.md](./Running_Unit_Tests.md) for instructions on running the tests.
5.  Write a first draft of the **User's Manual** describing the expected user interface (UI).
    *   You don't have a complete, working program yet; this is your best guess at what the program's interface will be like.
    *   The UI may change as you write code, but you should strive to make the design described by your manual.
6.  Fill out **Phase 1** in Plan.md.
    *   This will be the longest portion of the document.
7.  Track your time in Signature.md.
8.  **Tag** the last commit in this phase `designed`
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*


### Phase 2: Implementation (tag name `implemented`)
*(15% of your effort)*

**Finally, you can write code!**

0.  By the end of this phase the program is runnable.
    *   **Do not** move on if your program crashes unexpectedly!
    *   Don't forget to **close all files** your program uses.
1.  Update the **unit tests** to match your implementation.
    *   Tests will change as you find and fix problems with your program (or the tests themselves!)
    *   See [Running Unit Tests.md](./Running_Unit_Tests.md) for instructions on running the tests.
2.  Update the **UML class diagram** to match your implementation.
3.  Update your **User's manual** to match your implementation.
    *   Be sure to describe any error messages the user may see and explain how to get past them.
4.  Fill out **Phase 2** in Plan.md.
    *   As you work in this phase you may choose to deviate from the design you settled upon in the previous phase.  This is normal!
    *   Briefly explain what changed.
    *   Do not paste long passages of Python code in Plan.md.
    *   Your write-up for this phase may be very short.
5.  Track your time in Signature.md.
6.  **Tag** the last commit in this phase `implemented`


### Phase 3: Testing and Debugging (tag name `tested`)
*(30% of your effort)*

0.  All of your **unit tests** should pass by the end of this phase.
    *   See [Running Unit Tests.md](./Running_Unit_Tests.md) for instructions on running the tests.
1.  Fill out **Phase 3** in Plan.md.
    *   Describe the tests cases you ran, both automated unit tests as well as your own manual test cases.
    *   Make note of the commands that you ran and what happened in the program.
2.  If you found bugs in this phase, explain what was wrong and how you fixed it.
3.  Track your time in Signature.md.
4.  **Tag** the last commit in this phase `tested`


### Phase 4: Deployment (tag name `deployed`)
*(5% of your effort)*

It is your responsibility to ensure that your program will work on your grader's computer.

*   Code that crashes and *cannot* be quickly fixed by the grader will receive **0 points** on the relevant portions of the rubric.
*   Code that crashes but *can* be quickly fixed by the grader (or crashes only *some* of the time) will receive, at most, **half-credit** on the relevant portions of the rubric.

The following procedure is the best way for you to know what it will be like when the grader runs your code:

0.  Review [How to Submit this Assignment](./How_To_Submit.md) and make sure that your submission is correct.
1.  **Tag** the last commit in this phase `deployed`
    *   It is okay if this is the same commit that was tagged `tested`
2.  Push your code to GitLab, then check that all of your files, commits and **tags** appear there.
3.  Clone your project into a *different directory*, and re-run your test cases.
    *   Run `git log` and verify that all tags are present and on the correct commit.


### Phase 5: Maintenance

0.  Review your Plan.md and Signature.md one last time.
1.  Fill out **Phase 5** in Plan.md by answering the questions.
2.  Make one final commit and push your **completed** Software Development Plan and Signature to GitLab.
3.  Make sure that you are happy with your **Starter Code Quiz** score.
4.  Respond to the **Assignment Reflection Survey** on Canvas.


## What We Look for When Grading

**Total points: 110**

*   **Git Tags (5 points)**
    *   Each of these tags is present in your repository, and are placed on the right commits:
        0.  `analyzed`
        1.  `designed`
        2.  `implemented`
        3.  `tested`
        4.  `deployed` (may be on the same commit as `tested`)
*   **Quality documentation (35 points)**
    *   Plan.md
        *   Each section filled out with a convincing level of detail
        *   The design phase has Pseudocode instead of real code that was copied from the source files
    *   Signature.md
        *   All development activities are accounted for
        *   Placeholder entries and TODO notes removed
*   **C++ Team Documentation Review (10 points)**
    *   Write between **250-300 words** about the design documentation left by the C++ team
    *   Review committed on or before the `designed` tag
*   **UML Class Diagram (10 points)**
    *   Meets the standards explained in class
    *   At least two drafts (`designed` and `deployed`)
    *   Accurately represents the project at each stage
*   **User's manual (10 points)**
    *   At least two drafts (`designed` and `deployed`)
    *   Accurately represents the project at each stage
    *   Written at an appropriate level of detail for an end-user
*   **User Interface (10 points)**
    *   Menu options are case sensitive
        *   Error messages guide the user to give good input
    *   Prompts for numeric data
        *   Display the range of acceptable values
        *   Validate that the user's input is numeric and falls within the range
        *   Are repeated until the user provides correct input
        *   Error messages guide the user to give good input
    *   Prompts for string data
        *   Are repeated until the user provides non-empty input
        *   Error messages guide the user to give non-empty input
    *   Exceptions raised by `open()` are allowed to crash the program with a detailed stack trace
        *   In Python, files that don't exist are automatically created and existing files are overwritten when `open()` is called in write mode.
        *   It is the user's responsibility to provide a valid file name to the program.  You do not need to check that a file exists before calling `open()`.
*   **Program behavior (15 points)**
    *   The bug in the starter code is found and fixed
    *   Numbers are placed on cards according to requirements (numbers are randomized, column constraints are respected, Free! space in middle of odd-sized cards)
    *   Card ID and column headers ("BINGO ...") are displayed at the top of each card
    *   Cards persist until the Deck is destroyed
    *   "Save deck to file" function is realized; file object is closed afterward
*   **Unit tests (15 points)**
    *   Unit Tests meaningfully exercise the program's functions
    *   The 16 unit tests provided in the starter code pass:
        *   4 tests for the `Card` class that you must implement
        *   2 tests for the `Deck` class that you must implement
        *   3 tests for the `MenuOption` class provided by the C++ team
        *   3 tests for the `Menu` class provided by the C++ team
        *   4 tests for the `RandNumberSet` class provided by the C++ team
    *   New tests that you added beyond this list also pass


## Important Things to Watch Out For

0.  **100% penalty** your program imports any modules **except**:
    *   `math`
    *   `random`
    *   `sys`
    *   `time`
    *   `typing`
    *   `unittest`
    *   modules in the starter code
    *   new modules you wrote on your own
0.  **10 point penalty** an import statement fails due to misspelling or incorrect capitalization.
    *   **Windows users** make sure that the capitalization of your file names on GitLab matches your `import` statements!
0.  **10 point penalty** the program attempts to import a module from the `src.` package; this is the result of a PyCharm misconfiguration
0.  **10 point penalty** `eval()`, `exec()`, `globals()` or `locals()` are used.
    *   Instead of `eval()`, you should use `int()` instead.
0.  **10 point penalty** repository's URL on GitLab does not follow the naming convention
0.  **10 point penalty** repository is not a clone of the starter code
0.  **10 point penalty** required files or directories are missing, renamed or not in their expected locations
0.  **10 point penalty** `.gitignore` is missing or corrupt; forbidden files or directories are present in repository.  If you accidentally commit a huge CSV file, ask the instructor for help.
