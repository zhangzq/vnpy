import unittest
import korbit


class TestKorbit(unittest.TestCase):
    def setUp(self):
        pass

    def test_ticker(self):
        ticker = korbit.ticker()
        self.assertTrue('last' in list(ticker.keys()))
        self.assertTrue('timestamp' in list(ticker.keys()))
