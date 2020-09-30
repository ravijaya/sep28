import unittest
from os import listdir


def power(x, n):
    return  x ** n



class SampleTestCase(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_inequal(self):
        self.assertNotEqual(power(3, 2), 18)


class FileSystemTestCase(unittest.TestCase):
    def test_for_type(self):
        self.assertIs(type(listdir('/tmp')), dict)

if __name__ == '__main__':
    unittest.main()