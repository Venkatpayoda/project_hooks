'''
testcases
'''
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_add(self):
	self.assertTrue(5,10)

if __name__ == '__main__':
    unittest.main()
