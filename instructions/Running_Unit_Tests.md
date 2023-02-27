# CS 1440 Assignment 4: Bingo! - Running Unit Tests

The starter code consists of 16 test cases, 9 of which already pass.  You will increase the number of passing tests as you progress in the project.


## Running all test suites

*   You may run the unit tests through PyCharm or the shell.
*   To execute the tests from your shell, run `src/runTests.py`.  This script is a convenient way to execute all of the tests in one go.  It produces a lot of output:

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

The interpretation of this output is explained below.


## Running a single test suite

You may also execute an individual unit test suite.  Do this when you are focusing on just one part of the project and don't want to wade through unnecessary output.

The command to run a single suite is different than `runTests.py`.

1.  First, change into the `src/` directory 
2.  Then run this command, substituting the name of your desired test for `Testing/testMenu.py`
    *   ```bash
        $ cd src
        $ python -m unittest Testing/testMenu.py
        ...
        ----------------------------------------------------------------------
        Ran 3 tests in 0.000s

        OK
        ```


## Interpreting Test Results

A progress report is printed as tests are run.  When tests are unsuccessful, more text is printed to help you understand what exactly went wrong.  When many tests fail, you are presented with a lot of confusing text!

The starter code consists of 16 test cases, 9 of which already pass.  Of the 7 tests which don't pass, all *fail*, which means the tests don't see the expected results.  Another test result is *error*, which means that the code being tested crashed.  The dispositions of tests are summarized in this table:

Result | Meaning
-------|--------
`ok`   | The test passed
`FAIL` | The expected result was not seen
`ERROR`| The code under test crashed


### A passing test `ok`

When a test passes you are shown the name of the test method, the full name of the module it belongs to, and its docstring followed by `ok`

```
test_add_options (Testing.testMenu.TestMenu)
Ensure that options can be added to a Menu ... ok
```

### A failing test `FAIL`

A test that fails indicates that the code under test ran without crashing but did not yield the expected result.  After all tests have been run, a summary of the failure is printed which displays the line of the test file that failed and an explanation of the problem.  In this example, the `RandNumberSet` was not expected to return a set that contained the number `8`:

```
======================================================================
FAIL: test_noDuplicates (Testing.testRandNumberSet.TestRandNumberSet)
Ensure that a RandNumberSet contains no duplicates
----------------------------------------------------------------------
Traceback (most recent call last):
  File "src/Testing/testRandNumberSet.py", line 111, in test_noDuplicates
    self.assertNotIn(n, seen)
AssertionError: 8 unexpectedly found in {1, 2, 3, 4, 5, 6, 7, 8}
```

### A crashing test `ERROR`

The third way a test can conclude is by unexpectedly crashing (this means that there **is** a way to test a function that is *supposed* to crash; read the `unittest` documentation if you are curious).  In this example an index that is too large for the list `j` is used, causing the tested method to crash.  The line of the unit test where the crash happened is shown, and below that you can see the line from which the crash originated, leading you right to the bug:

```
======================================================================
ERROR: test_chCommand (Testing.testMenuOption.TestMenuOption)
Ensure each option's letter char is set correctly
----------------------------------------------------------------------
Traceback (most recent call last):
  File "src/Testing/testMenuOption.py", line 40, in test_chCommand
    self.assertEqual(self.a.getCommand(), "A")
  File "src/MenuOption.py", line 54, in getCommand
    j[11] += 1
IndexError: list index out of range
```
