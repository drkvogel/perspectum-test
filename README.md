# perspectum-test

Perspectum Diagnostics pre-interview task

## Brief - Test Lead (Python)

Task Implementation

Write a script containing a Python function which accepts any number of lists (1..n) as parameters, assuming the lists only contain character strings (e.g. `['a', 'b', 'bc']).`

The function should print out the following: -
    Strings that appear in more than one list -
    The total number of unique strings across all lists -
    The total number of strings that were processed

Test Case

Write at least one test case, ensuring the example case below is verified:

Input

    ['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn']

Output

    Strings appearing in multiple lists: 'gh'
    Number of unique strings: 7
    Total number of strings processed: 9

Please use either Bitbucket/GitHub, or provide a ZIP containing the application code

## Files

`analyse_lists.py` contains the list-analysing function `analyse()`

`test_analyse_lists.py` contains automation tests in the `unittest` framework (also compatible with `pytest`, `nosetests` etc)

## Running

Run `./analyse_tests.py` to run some simple tests.

Run `./test_analyse_lists.py` to run unit tests.
