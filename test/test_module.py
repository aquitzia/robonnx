import unittest

class SampleTest(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('abc'.upper(), 'ABC')
    def test_lower(self):
        self.assertEqual('ABC'.lower(), 'abc')