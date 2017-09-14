#!/usr/bin/python

import analyse_lists
import unittest

import StringIO
import sys

class TestAnalyseLists(unittest.TestCase):
    # def test_test(self):
    #     # pass
    #     self.assertEqual(1, 1)

    # def test_1(self):
    #     analyse_lists.analyse(['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'])

    # def test_2(self):
    #     analyse_lists.analyse(['g', 'gh', 'ghj', 'g', 'hh'], ['j', 'ju', 'gh', 'gk', 'gn'], ['g', 'ju', 'hh', 'hh'])

    def test_3(self):
        capturedOutput = StringIO.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput                   #  and redirect stdout.
        analyse_lists.analyse(['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'])
        sys.stdout = sys.__stdout__                   # Reset redirect.
        expected = """Strings appearing in multiple lists: , 'gh'
Number of unique strings: 7
Strings processed: 9
"""
        print 'Expected: ', expected
        print "END"
        print 'Captured: ', capturedOutput.getvalue()
        print "END"
        print _unidiff_output(expected, capturedOutput.getvalue())
        self.assertTrue(expected == capturedOutput.getvalue())

    # def test_4(self):
    #     self.assertTrue(1 == 2)
    # def test_5(self):
    #     self.assertTrue(1 == 2)
    # def test_6(self):
    #     self.assertTrue(1 == 2)

def _unidiff_output(expected, actual):
    """
    Helper function. Returns a string containing the unified diff of two multiline strings.
    """

    import difflib
    expected=expected.splitlines(1)
    actual=actual.splitlines(1)

    diff=difflib.unified_diff(expected, actual)

    return ''.join(diff)


if __name__ == '__main__':
    print "starting"
    unittest.main()
    print "finished"