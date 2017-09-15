#!/usr/bin/python

import unittest
import StringIO
import sys
import analyse_lists

class TestAnalyseLists(unittest.TestCase):

    def setUp(self):
        self.captured = StringIO.StringIO()
        sys.stdout = self.captured

    def tearDown(self):
        sys.stdout = sys.__stdout__
        # print 'Expected: \"'+ repr(self.expected) + '\"'
        # print 'Captured: \"'+ repr(self.captured.getvalue()) + '\"'

    def test_1(self):
        analyse_lists.analyse(['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'])
        self.expected = """Strings appearing in multiple lists: 'gh'
Number of unique strings: 7
Strings processed: 9
"""
        self.assertTrue(self.expected == self.captured.getvalue())

    def test_2(self):
        analyse_lists.analyse(['g', 'gh', 'ghj', 'g', 'hh'], ['j', 'ju', 'gh', 'gk', 'gn'], ['g', 'ju', 'hh', 'hh'])
        self.expected = """Strings appearing in multiple lists: 'g', 'ju', 'hh', 'gh'
Number of unique strings: 8
Strings processed: 14
"""
        self.assertTrue(self.expected == self.captured.getvalue())

    def test_3(self):
        analyse_lists.analyse(['g', 'gh', 'ghj', 'g', 'hh'])
        self.expected = """Strings appearing in multiple lists: 
Number of unique strings: 4
Strings processed: 5
"""
        self.assertTrue(self.expected == self.captured.getvalue())

    def test_4(self):
        analyse_lists.analyse(['x', 'y', 'z', 'z'], ['a', 'b', 'c', 'cc', 'ccc'], ['e', 'f', 'g', 'cc'], ['h', 'i', 'j', 'jj', 'jjj'], ['j', 'jj', 'jjj', 'cc', 'a'])
        self.expected = """Strings appearing in multiple lists: 'a', 'cc', 'j', 'jjj', 'jj'
Number of unique strings: 16
Strings processed: 23
"""
        self.assertTrue(self.expected == self.captured.getvalue())

    def test_no_lists(self):
        analyse_lists.analyse()
        self.expected = """Strings appearing in multiple lists: 
Number of unique strings: 0
Strings processed: 0
"""
        self.assertTrue(self.expected == self.captured.getvalue())

    def test_empty_lists(self):
        analyse_lists.analyse(['a', 'b'], [], [], ['b', 'c'], [], ['b'])
        self.expected = """Strings appearing in multiple lists: 'b'
Number of unique strings: 3
Strings processed: 5
"""
        self.assertTrue(self.expected == self.captured.getvalue())

if __name__ == '__main__':
    unittest.main()
