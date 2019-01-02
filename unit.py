import unittest
import xmlrunner

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual( multiply(3,4), 12)

    def test_strings_a_3(self):
        self.assertEqual( multiply('a',3), 'aaa')

    def test_strings_a_3(self):
        self.assertEqual( multiply(3,3), 9)

def multiply(a,b):
 return a * b


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='./test_result'))
