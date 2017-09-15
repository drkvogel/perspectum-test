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
    unique_strings = []
    occurrence_count = {}

    for a_list in lists:
        for string in a_list:
            all_strings.append(string)
    unique_strings = set(all_strings) # set of unique strings

    # build list of lists where strings are unique in each list
    lists_unique = list()
    for i in range(0, len(lists)):
        lists_unique.append(set(lists[i])) #

    # count occurrences of each string across all lists (containing unique strings)
    occurrence_count = dict()
    for a_list in lists_unique:
        for el in a_list:
            if el not in occurrence_count.keys():
                occurrence_count[el] = 1
            else:
                occurrence_count[el] = occurrence_count[el] + 1
    multiple_occurrence = multiple_occurrence_generator(occurrence_count)

    print 'Strings appearing in multiple lists:', # join() leaves trailing space so omit here
    print ', '.join('\'' + item + '\'' for item in multiple_occurrence) # add quotes for each item and join with comma
    print 'Number of unique strings: ' + str(len(unique_strings))
    print 'Strings processed: ' + str(len(all_strings))

def multiple_occurrence_generator(occurrence_count):
    """generator to list strings that appear more than once"""
    for i, key in enumerate(occurrence_count):
        if occurrence_count[key] > 1:
            yield key

def test():
    analyse(['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'])
    analyse(['g', 'gh', 'ghj', 'g', 'hh'], ['j', 'ju', 'gh', 'gk', 'gn'], ['g', 'ju', 'hh', 'hh'])
    analyse(['g', 'gh', 'ghj', 'g', 'hh'])
    analyse(['a', 'b'], [], [], ['b', 'c', 'a'], [], ['b'])

if __name__ == '__main__':
    test()

# print "occurrence_count: " + str(occurrence_count)
# print 'Input: ' + str(lists)

    # print ', '.join([])

    # print from generator
    # occurrence_generator = multiple_occurrence(occurrence_count)
    # for i, key in enumerate(occurrence_generator):
    #     if i > 0:
    #         sys.stdout.write(', ') 
    #     sys.stdout.write('\'' + key + '\'') # no space, no newline
    # print

    # for i, key in enumerate(occurrence_count):
    #     if occurrence_count[key] > 1:
    #         if i > 0:
    #             sys.stdout.write(', ') # no space, no newline
    #         sys.stdout.write('\'' + key + '\'')
