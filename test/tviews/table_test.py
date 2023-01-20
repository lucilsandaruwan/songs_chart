import views.table as tbl 
import unittest

class TestChartModel(unittest.TestCase):

    def testLengthOfTableColumns(self):
        print("Testing table column length")
        # column length les than 3 letters
        result = tbl.length_of_table_columns("No")
        self.assertEqual(result, 5)
        # column length is greater than 3
        result = tbl.length_of_table_columns("No of times")
        self.assertEqual(result, 13)
        
if __name__ == '__main__':
    unittest.main()