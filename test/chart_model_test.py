import unittest
import sys
sys.path.append('../')
from chart_model import get_file_handler, init_list, get_as_a_list
import csv
import io

class TestChartModel(unittest.TestCase):

    def testFileHandler(self):
        print("Test csv file connection")
        connection = get_file_handler()
        if type(connection) == io.TextIOWrapper:
            connection.close()
        self.assertIs(type(connection), io.TextIOWrapper)

    def testInitList(self):
        print("Test the number of records in chart than 0")
        init_list()
        l = get_as_a_list()
        self.assertGreater(len(l), 0)
        
if __name__ == '__main__':
    unittest.main()