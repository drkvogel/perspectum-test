#!/usr/bin/python

import unittest
import StringIO
import sys
import analyse_lists

class TestAnalyseLists(unittest.TestCase):

    # def unidiff_output(self, expected, actual):
    #     """
    #     Helper function for development. Returns a string containing the unified diff of two multiline strings.
    #     """
    #     import difflib
    #     expected = expected.splitlines(1)
    #     actual = actual.splitlines(1)
    #     diff = difflib.unified_diff(expected, actual)
    #     return ''.join(diff)

    def test_1(self):
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        analyse_lists.analyse(['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'])
        sys.stdout = sys.__stdout__
        expected = """Strings appearing in multiple lists: , 'gh'
Number of unique strings: 7
Strings processed: 9
"""
        self.assertTrue(expected == capturedOutput.getvalue())

    def test_2(self):
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        analyse_lists.analyse(['g', 'gh', 'ghj', 'g', 'hh'], ['j', 'ju', 'gh', 'gk', 'gn'], ['g', 'ju', 'hh', 'hh'])
        sys.stdout = sys.__stdout__
        expected = """Strings appearing in multiple lists: 'g', 'ju', 'hh', 'gh'
Number of unique strings: 8
Strings processed: 14
"""
        # print _unidiff_output(expected, capturedOutput.getvalue())
        self.assertTrue(expected == capturedOutput.getvalue())

    def test_3(self):
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        analyse_lists.analyse(['g', 'gh', 'ghj', 'g', 'hh'])
        sys.stdout = sys.__stdout__
        expected = """Strings appearing in multiple lists: 
Number of unique strings: 4
Strings processed: 5
"""
        self.assertTrue(expected == capturedOutput.getvalue())

    def test_4(self):
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        analyse_lists.analyse(['x', 'y', 'z', 'z'], ['a', 'b', 'c', 'cc', 'ccc'], ['e', 'f', 'g', 'cc'], ['h', 'i', 'j', 'jj', 'jjj'], ['j', 'jj', 'jjj', 'cc', 'a'])
        sys.stdout = sys.__stdout__
        expected = """Strings appearing in multiple lists: 'a', 'cc', 'j', 'jjj', 'jj'
Number of unique strings: 16
Strings processed: 23
"""
        self.assertTrue(expected == capturedOutput.getvalue())

    def test_5(self):
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        analyse_lists.analyse()
        sys.stdout = sys.__stdout__
        expected = """Strings appearing in multiple lists: 
Number of unique strings: 0
Strings processed: 0
"""
        self.assertTrue(expected == capturedOutput.getvalue())


if __name__ == '__main__':
    unittest.main()
