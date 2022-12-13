import unittest
import sys
sys.path.append('../')
from chart_report import get_first_n_letters
import csv
import io

class TestChartReport(unittest.TestCase):

    def testGestFirstNLetters(self):
        print("Test y-axis text splitter")
        string = "0123456"
        number = 5
        returnValue = get_first_n_letters(string, number)
        print(returnValue)
        self.assertEqual("01234...", returnValue)
        
if __name__ == '__main__':
    unittest.main()