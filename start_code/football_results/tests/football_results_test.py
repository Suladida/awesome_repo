import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    def setUp(self):
        self.result_1 = {    
    "home_score": 1,
    "away_score": 0
    }

        self.result_2 = {    
    "home_score": 0,
    "away_score": 1
    }

        self.result_3 = {    
    "home_score": 2,
    "away_score": 2
    }

    # Test we get the right result string for a final score dictionary representing -
    def test_get_result(self):
    # Home win
        home_win = get_result(self.result_1)
        self.assertEqual("Home win", home_win)
        # Away win
        away_win = get_result(self.result_2)
        self.assertEqual("Away win", away_win)
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 


if __name__ == "__main__":
    unittest.main()
