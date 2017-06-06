'''
testcases
'''
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())

    def test_add(self):
	self.assertEqual(5,10)
	self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
