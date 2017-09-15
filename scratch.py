#!/usr/bin/python
#!/usr/bin/env python

'''
Scratch file for development
'''

# print "Hello, World!"
import sys # for sys.stdout.write
import analyse_lists
import StringIO

def analyse_lists_local(*lists):
    # count = 0
    # more_than_once = 0
    # more_than_once = []
    all_strings = []
    list_unique = {}
    occurrence_count = {}
    for lista in lists:
        # print list
        for el in lista:
            # print el
            # count = count + 1
            if el not in occurrence_count.keys():
                occurrence_count[el] = 1
            else:
                occurrence_count[el] = occurrence_count[el] + 1
            all_strings.append(el)
            # if el in all_strings and el not in more_than_once:
            #     # more_than_once = more_than_once + 1 # incorrect, will count too many if el in 3 or more lists
            #     more_than_once.append(el) # wrong
    list_unique = set(all_strings)

    # for list in lists:
    # #     # print list
    #     list = set(list)
    # for i, lista in enumerate(lists):
        # lists[i] = set(lista) #set(list)
    # print(list) # <type 'list'>
    # temp = set()
    temp = list()
    for i in range(0, len(lists)):
        # lists[i] = list(lists[i]) #set(list)
        # temp.add(set(lists[i]))
        temp.append(set(lists[i]))
        # print set(lists[i])
        # print list(lists[i])
        # lists[i] = set(lists[i])
        # lists[i] = list(lists[i])

    # for i in range(len(temp))
    occurrence_count = dict()

    for lista in temp:
        # print 'lista: ' + str(lista)
        for el in lista:
            if el not in occurrence_count.keys():
                occurrence_count[el] = 1
            else:
                occurrence_count[el] = occurrence_count[el] + 1

    # for el in list:
    #         print el
    #         count = count + 1
    #         all_strings.append(el)

    print 'Input: ' + str(lists)
    # print 'all_strings: ' + str(all_strings)
    # still not right as two or more identical strings in the same list is a false positive
    print 'len(occurrence_count): ' + str(len(occurrence_count))
    print 'Strings appearing in multiple lists: ',# + str(more_than_once)
    # for key in occurrence_count:
    #     if occurrence_count[key] > 1:
    #         print "'" + key + "', ",
    for i, key in enumerate(occurrence_count):
        if occurrence_count[key] > 1:
            if i > 0:
                # print (', ', end='') # python 3
                # print ', ',
                sys.stdout.write(', ')
            # print(key, end='')
            sys.stdout.write('\'' + key + '\'')
        #     print "'" + key + "', ",

            # if i == len(occurrence_count) - 1:
            #     print "'" + key + "', "
            # else:
            #     print "'" + key + "', ",
    print
    print 'Number of unique strings: ' + str(len(list_unique))
    # print 'Strings processed: ' + str(count)
    print 'Strings processed: ' + str(len(all_strings))
    print

def unidiff_output(self, expected, actual):
    """
    Helper function for development. Returns a string containing the unified diff of two multiline strings.
    """
    import difflib
    expected = expected.splitlines(1)
    actual = actual.splitlines(1)
    diff = difflib.unified_diff(expected, actual)
    return ''.join(diff)

def capture_output(func, *args):
    capturedOutput = StringIO.StringIO()          # create StringIO object
    sys.stdout = capturedOutput                   # redirect stdout.
    func(args)
    # analyse_lists.analyse(['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'])
    sys.stdout = sys.__stdout__                   # reset redirect
    return capturedOutput.getvalue()

# analyse_lists_local(['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'])
# analyse_lists_local(['g', 'gh', 'ghj', 'g', 'hh'], ['j', 'ju', 'gh', 'gk', 'gn'], ['g', 'ju', 'hh', 'hh'])
# captured = capture_output(analyse_lists.analyse, ['g', 'gh', 'ghj', 'g'], ['j',  'ju', 'gh', 'gk', 'gn'])    capturedOutput = StringIO.StringIO()          # create StringIO object
capturedOutput = StringIO.StringIO()          # create StringIO object
sys.stdout = capturedOutput                   # redirect stdout.
analyse_lists.analyse(['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'])
# analyse_lists.analyse(['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'])
sys.stdout = sys.__stdout__                   # reset redirect

# print 'Expected: ', expected
# print "END"
print 'Captured: ', repr(capturedOutput.getvalue())
print "END"
# print unidiff_output(expected, capturedOutput.getvalue())
# print captured

    # def test_2(self):
#     def test_captured(self):
#         # captured = capture_output(analyse_lists.analyse(['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn']))
#         captured = self.capture_output(analyse_lists.analyse, ['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'])
#         expected = """Strings appearing in multiple lists: , 'gh'
# Number of unique strings: 7
# Strings processed: 9
# """
#         self.assertTrue(expected == captured)

# print 'Expected: \"'+ repr(expected) + '\"'
# print "END"
# print 'Captured: \"'+ repr(capturedOutput.getvalue()) + '\"'
# print "END"
# print "len(capturedOutput.getvalue()): " + str(len(capturedOutput.getvalue()))
# print "type(capturedOutput.getvalue()): " + str(type(capturedOutput.getvalue()))
# print self.unidiff_output(expected, capturedOutput.getvalue())
