#!/usr/bin/python
    # works on laptop vbox
#!/usr/bin/env python
    # doesn't work on laptop vbox

'''
Brief - Test Lead (Python)

Task Implementation

Write a script containing a Python function which accepts any number of lists (1..n) as parameters, assuming the lists only contain character strings (e.g. ['a', 'b', 'bc']).

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
'''

import sys # for sys.stdout.write

def analyse(*lists):
    all_strings = []
    list_unique = {}
    occurrence_count = {}

    for lista in lists:
        for el in lista:
            all_strings.append(el)
    list_unique = set(all_strings)

    temp = list()
    for i in range(0, len(lists)):
        temp.append(set(lists[i])) #

    occurrence_count = dict()
    for lista in temp:
        for el in lista:
            if el not in occurrence_count.keys():
                occurrence_count[el] = 1
            else:
                occurrence_count[el] = occurrence_count[el] + 1

    print 'Input: ' + str(lists)
    print 'Strings appearing in multiple lists: ',# + str(more_than_once)
    for i, key in enumerate(occurrence_count):
        if occurrence_count[key] > 1:
            if i > 0:
                sys.stdout.write(', ') # no space, no newline
            sys.stdout.write('\'' + key + '\'')

    print
    print 'Number of unique strings: ' + str(len(list_unique))
    print 'Strings processed: ' + str(len(all_strings))

def test():
    analyse(['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'])
    analyse(['g', 'gh', 'ghj', 'g', 'hh'], ['j', 'ju', 'gh', 'gk', 'gn'], ['g', 'ju', 'hh', 'hh'])
    analyse(['g', 'gh', 'ghj', 'g', 'hh'])

if __name__ == '__main__':
    test()
