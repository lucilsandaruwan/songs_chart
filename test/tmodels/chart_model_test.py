import unittest
import models.chart_csv as cc
import csv
import io

class TestChartModel(unittest.TestCase):
    # TODO: Need to implement unit tests for the remaining functions of this model also.
    # Those are not implemented as it is required more time 

    def testFileHandler(self):
        print("Test csv file connection")
        connection = cc.get_file_handler()
        if type(connection) == io.TextIOWrapper:
            connection.close()
        self.assertIs(type(connection), io.TextIOWrapper)

    def testInitList(self):
        print("Test the number of records in chart than 0")
        cc.init_list()
        l = cc.get_as_a_list()
        self.assertGreater(len(l), 0)
    
    def testTop10Songs(self):
        """ this is to test the top_10_songs function
        """
        # test empty data set
        cc.set_chart_list([])
        top_10 = cc.top_10_songs()
        self.assertEqual(top_10, [])

        # Check resuls when rank 1 and 2 has data from two days but different climbs
        data = [
            {'date': '2021-11-06', 'rank': '1', 'song': 'Easy On Me61', 'artist': 'Adele1', 'last-week': '1' }
            ,{'date': '2021-11-06', 'rank': '2', 'song': 'Stay62', 'artist': 'The Kid LAROI & Justin Bieber2', 'last-week': '2' }
            ,{'date': '2021-11-06', 'rank': '3', 'song': 'Stay63', 'artist': 'The Kid LAROI & Justin Bieber3', 'last-week': '8' }
            ,{'date': '2021-11-06', 'rank': '4', 'song': 'Stay64', 'artist': 'The Kid LAROI & Justin Bieber4', 'last-week': '2' }
            ,{'date': '2021-11-06', 'rank': '5', 'song': 'Stay65', 'artist': 'The Kid LAROI & Justin Bieber5', 'last-week': '2' }
            ,{'date': '2021-11-06', 'rank': '6', 'song': 'Stay66', 'artist': 'The Kid LAROI & Justin Bieber6', 'last-week': '2' }
            ,{'date': '2021-11-06', 'rank': '7', 'song': 'Stay67', 'artist': 'The Kid LAROI & Justin Bieber7', 'last-week': '10' }
            ,{'date': '2021-11-06', 'rank': '8', 'song': 'Stay68', 'artist': 'The Kid LAROI & Justin Bieber8', 'last-week': '2' }
            ,{'date': '2021-11-06', 'rank': '9', 'song': 'Stay69', 'artist': 'The Kid LAROI & Justin Bieber9', 'last-week': '2' }
            ,{'date': '2021-11-06', 'rank': '10', 'song': 'Stay610', 'artist': 'The Kid LAROI & Justin Bieber10', 'last-week': '2' }
            ,{'date': '2021-11-07', 'rank': '1', 'song': 'Stay71', 'artist': 'The Kid LAROI & Justin Bieber71', 'last-week': '2' }
            ,{'date': '2021-11-07', 'rank': '2', 'song': 'Stay72', 'artist': 'The Kid LAROI & Justin Bieber72', 'last-week': '4' }

        ]
        expected = [
            {'artist': 'The Kid LAROI & Justin Bieber71', 'song': 'Stay71', 'number_of_top_times': 1, 'climb': 1}
            , {'artist': 'Adele1', 'song': 'Easy On Me61', 'number_of_top_times': 1, 'climb': 0}
            , {'artist': 'The Kid LAROI & Justin Bieber72', 'song': 'Stay72', 'number_of_top_times': 1, 'climb': 2}
            , {'artist': 'The Kid LAROI & Justin Bieber2', 'song': 'Stay62', 'number_of_top_times': 1, 'climb': 0}
            , {'artist': 'The Kid LAROI & Justin Bieber3', 'song': 'Stay63', 'number_of_top_times': 1, 'climb': 5}
            , {'artist': 'The Kid LAROI & Justin Bieber4', 'song': 'Stay64', 'number_of_top_times': 1, 'climb': -2}
            , {'artist': 'The Kid LAROI & Justin Bieber5', 'song': 'Stay65', 'number_of_top_times': 1, 'climb': -3}
            , {'artist': 'The Kid LAROI & Justin Bieber6', 'song': 'Stay66', 'number_of_top_times': 1, 'climb': -4}
            , {'artist': 'The Kid LAROI & Justin Bieber7', 'song': 'Stay67', 'number_of_top_times': 1, 'climb': 3}
            , {'artist': 'The Kid LAROI & Justin Bieber8', 'song': 'Stay68', 'number_of_top_times': 1, 'climb': -6}
            , {'artist': 'The Kid LAROI & Justin Bieber9', 'song': 'Stay69', 'number_of_top_times': 1, 'climb': -7}
            , {'artist': 'The Kid LAROI & Justin Bieber10', 'song': 'Stay610', 'number_of_top_times': 1, 'climb': -8}
        ]
        cc.set_chart_list(data)
        result = cc.top_10_songs()
        self.assertEqual(result, expected)
        # Check resuls when rank 1 has data from different days but same climbs
        # Did not change the date as it is not considered
        data = [
            {'date': '2021-11-06', 'rank': '1', 'song': 'Easy On Me61', 'artist': 'Adele1', 'last-week': '1', 'peak-rank': '1', }
            ,{'date': '2021-11-06', 'rank': '1', 'song': 'Stay62', 'artist': 'The Kid LAROI & Justin Bieber2', 'last-week': '2'}
            ,{'date': '2021-11-06', 'rank': '1', 'song': 'Stay63', 'artist': 'The Kid LAROI & Justin Bieber3', 'last-week': '8'}
            ,{'date': '2021-11-06', 'rank': '1', 'song': 'Stay64', 'artist': 'The Kid LAROI & Justin Bieber4', 'last-week': '2'}
            ,{'date': '2021-11-06', 'rank': '1', 'song': 'Stay65', 'artist': 'The Kid LAROI & Justin Bieber5', 'last-week': '2'}
            ,{'date': '2021-11-06', 'rank': '1', 'song': 'Stay66', 'artist': 'The Kid LAROI & Justin Bieber6', 'last-week': '2'}
            ,{'date': '2021-11-06', 'rank': '1', 'song': 'Stay67', 'artist': 'The Kid LAROI & Justin Bieber7', 'last-week': '10'}
            ,{'date': '2021-11-06', 'rank': '1', 'song': 'Stay68', 'artist': 'The Kid LAROI & Justin Bieber8', 'last-week': '2'}
            ,{'date': '2021-11-06', 'rank': '1', 'song': 'Stay69', 'artist': 'The Kid LAROI & Justin Bieber9', 'last-week': '2'}
            ,{'date': '2021-11-06', 'rank': '1', 'song': 'Stay610', 'artist': 'The Kid LAROI & Justin Bieber10', 'last-week': '2'}
            ,{'date': '2021-11-06', 'rank': '1', 'song': 'Stay71', 'artist': 'The Kid LAROI & Justin Bieber71', 'last-week': '2'}
            ,{'date': '2021-11-06', 'rank': '1', 'song': 'Stay72', 'artist': 'The Kid LAROI & Justin Bieber72', 'last-week': '4'}

        ]
        # all the record should be there because some climbs are equal in top 10 ranks
        expected = [{'artist': 'The Kid LAROI & Justin Bieber7', 'song': 'Stay67', 'number_of_top_times': 1, 'climb': 9}
        , {'artist': 'The Kid LAROI & Justin Bieber3', 'song': 'Stay63', 'number_of_top_times': 1, 'climb': 7}
        , {'artist': 'The Kid LAROI & Justin Bieber72', 'song': 'Stay72', 'number_of_top_times': 1, 'climb': 3}
        , {'artist': 'The Kid LAROI & Justin Bieber2', 'song': 'Stay62', 'number_of_top_times': 1, 'climb': 1}
        , {'artist': 'The Kid LAROI & Justin Bieber4', 'song': 'Stay64', 'number_of_top_times': 1, 'climb': 1}
        , {'artist': 'The Kid LAROI & Justin Bieber5', 'song': 'Stay65', 'number_of_top_times': 1, 'climb': 1}
        , {'artist': 'The Kid LAROI & Justin Bieber6', 'song': 'Stay66', 'number_of_top_times': 1, 'climb': 1}
        , {'artist': 'The Kid LAROI & Justin Bieber8', 'song': 'Stay68', 'number_of_top_times': 1, 'climb': 1}
        , {'artist': 'The Kid LAROI & Justin Bieber9', 'song': 'Stay69', 'number_of_top_times': 1, 'climb': 1}
        , {'artist': 'The Kid LAROI & Justin Bieber10', 'song': 'Stay610', 'number_of_top_times': 1, 'climb': 1}
        , {'artist': 'The Kid LAROI & Justin Bieber71', 'song': 'Stay71', 'number_of_top_times': 1, 'climb': 1}
        , {'artist': 'Adele1', 'song': 'Easy On Me61', 'number_of_top_times': 1, 'climb': 0}]

        cc.set_chart_list(data)
        result = cc.top_10_songs()
        self.assertEqual(result, expected)
        
if __name__ == '__main__':
    unittest.main()