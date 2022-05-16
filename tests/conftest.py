import unittest
from src.MWParser import MWParser


class ParserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = MWParser("./cached")

    def assertParsed(self, wikitext, expected_data):
        result = self.parser.parse_wikicode(wikitext)
        self.assertEqual(expected_data, result.text)
