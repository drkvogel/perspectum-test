#!/usr/bin/python

import unittest
import StringIO
import sys
import analyse_lists

class TestAnalyseLists(unittest.TestCase):
    # def test_1(self):
    #     analyse_lists.analyse(['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'])

    # def test_2(self):
    #     analyse_lists.analyse(['g', 'gh', 'ghj', 'g', 'hh'], ['j', 'ju', 'gh', 'gk', 'gn'], ['g', 'ju', 'hh', 'hh'])


    def test_1(self):
        capturedOutput = StringIO.StringIO()          # create StringIO object
        sys.stdout = capturedOutput                   # redirect stdout.
        analyse_lists.analyse(['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'])
        sys.stdout = sys.__stdout__                   # reset redirect
        expected = """Strings appearing in multiple lists: , 'gh'
Number of unique strings: 7
Strings processed: 9
"""
        print 'Expected: ', expected
        print "END"
        print 'Captured: ', capturedOutput.getvalue()
        print "END"
        # print _unidiff_output(expected, capturedOutput.getvalue())
        self.assertTrue(expected == capturedOutput.getvalue())

    def test_2(self):
        capturedOutput = StringIO.StringIO()          # create StringIO object
        sys.stdout = capturedOutput                   # redirect stdout.
        analyse_lists.analyse(['g', 'gh', 'ghj', 'g', 'hh'], ['j', 'ju', 'gh', 'gk', 'gn'], ['g', 'ju', 'hh', 'hh'])
        sys.stdout = sys.__stdout__                   # reset redirect
        expected = """Strings appearing in multiple lists: 'g', 'ju', 'hh', 'gh'
Number of unique strings: 8
Strings processed: 14
"""
        print 'Expected: ', expected
        print "END"
        print 'Captured: ', capturedOutput.getvalue()
        print "END"
        # print _unidiff_output(expected, capturedOutput.getvalue())
        self.assertTrue(expected == capturedOutput.getvalue())

    def unidiff_output(self, expected, actual):
        """
        Helper function for development. Returns a string containing the unified diff of two multiline strings.
        """
        import difflib
        expected = expected.splitlines(1)
        actual = actual.splitlines(1)
        diff = difflib.unified_diff(expected, actual)
        return ''.join(diff)

    def test_3(self):
        capturedOutput = StringIO.StringIO()          # create StringIO object
        sys.stdout = capturedOutput                   # redirect stdout.
        analyse_lists.analyse(['g', 'gh', 'ghj', 'g', 'hh'])
        sys.stdout = sys.__stdout__                   # reset redirect
        expected = """Strings appearing in multiple lists: 
Number of unique strings: 4
Strings processed: 5
"""
        print 'Expected: \"'+ repr(expected) + '\"'
        print "END"
        print 'Captured: \"'+ repr(capturedOutput.getvalue()) + '\"'
        print "END"
        print "len(capturedOutput.getvalue()): " + str(len(capturedOutput.getvalue()))
        print "type(capturedOutput.getvalue()): " + str(type(capturedOutput.getvalue()))
        print self.unidiff_output(expected, capturedOutput.getvalue())

        self.assertTrue(expected == capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main()
