from .conftest import ParserTestCase


class FormattingTestCase(ParserTestCase):
    def test_italic(self):
        wikitext = "''Test''"
        self.assertParsed(wikitext, ["Test"])
