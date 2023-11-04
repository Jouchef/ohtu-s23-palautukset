import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_top_two(self):
        toptwo = self.stats.top(2)

        expected = [
        Player("Gretzky", "EDM", 35, 89),
        Player("Lemieux", "PIT", 45, 54)
    ]

        self.assertEqual(toptwo, expected)


    def test_search_player_will_be_found(self):
        result = self.stats.search("Semenko")

        self.assertEqual(result, Player("Semenko", "EDM", 4, 12))


    def test_search_player_not_found(self):
        result = self.stats.search("Joona")

        self.assertEqual(result, None)

    def test_team_returns_correctly(self):
        team = self.stats.team("PIT")

        expected = [
            Player("Lemieux", "PIT", 45, 54)
        ]

        self.assertEqual(team, expected)
