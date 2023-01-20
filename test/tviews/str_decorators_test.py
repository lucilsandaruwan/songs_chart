import views.str_decorators as strd 
import configs.meta as m
import unittest

class TestChartModel(unittest.TestCase):

    def testFormat(self):
        stls = m.get_config("str_styles")
        print("Testing the srting format")
        stls = stls if stls else {}
        for key, val in stls.items():
            result = strd.format("test msg", key)
            expected = val + "test msg" + '\033[0m'
            self.assertEqual(result, expected)
        
if __name__ == '__main__':
    unittest.main()

    