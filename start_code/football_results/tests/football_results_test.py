import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    def setUp(self):
        self.final_scores = [
            {    
                "home_score": 1,
                "away_score": 0
            },
            {    
                "home_score": 0,
                "away_score": 1
            },
            {    
                "home_score": 2,
                "away_score": 2
            }
        ]

    # Test we get the right result string for a final score dictionary representing -
    def test_get_result(self):
    # Home win
        home_win = get_result(self.final_scores[0])
        self.assertEqual("Home win", home_win)
        # Away win
        away_win = get_result(self.final_scores[1])
        self.assertEqual("Away win", away_win)
        # Draw
        draw = get_result(self.final_scores[2])
        self.assertEqual("Draw", draw)

    # Test we get right list of result strings for a list of final score dictionaries.
    def test_get_results(self):
        all_scores = get_results(self.final_scores)
        self.assertEqual(["Home win", "Away win", "Draw"], all_scores)


if __name__ == "__main__":
    unittest.main()
