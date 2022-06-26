import unittest
from WHParallelParser import WHParallelParser


class ParserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = WHParallelParser(cache_folder="./tests/cached")

    def assertParsed(self, wikitext, expected_data):
        result = self.parser.parse_wikicode(wikitext)
        self.assertEqual(expected_data, result.text)

    def assertTags(self, wikitext, expected_data, expected_tag):
        result = self.parser.parse_wikicode(wikitext)
        self.assertEqual(expected_data, result.find_first_tag(expected_tag))
