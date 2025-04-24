import unittest
from main import countc
class TestCountC(unittest.TestCase):
    def test_simple(self):
        s = 'milad shahkarami'
        c = 'a'
        result = 4
        self.assertEqual(countc(s ,c), result)
    def test_all(self):
        s = 'mmmmmmmm'
        c = 'm'
        self.assertEqual(countc(s,c),8)
if __name__ == '__main__':
    unittest.main()
