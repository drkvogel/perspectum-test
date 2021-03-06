#!/usr/bin/python
    # works on laptop vbox
#!/usr/bin/env python
    # doesn't work on laptop vbox

import sys # for sys.stdout.write

def analyse(*lists):
    all_strings = []
    unique_strings = []
    occurrence_count = {}
    lists_unique = list()

    for a_list in lists:
        lists_unique.append(set(a_list)) # build list of lists where strings are unique in each list
        for string in a_list:
            all_strings.append(string)
    unique_strings = set(all_strings) # set of unique strings

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

def demo():
    analyse(['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'])
    analyse(['g', 'gh', 'ghj', 'g', 'hh'], ['j', 'ju', 'gh', 'gk', 'gn'], ['g', 'ju', 'hh', 'hh'])
    analyse(['g', 'gh', 'ghj', 'g', 'hh'])
    analyse(['a', 'b'], [], [], ['b', 'c', 'a'], [], ['b'])

if __name__ == '__main__':
    demo()

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
