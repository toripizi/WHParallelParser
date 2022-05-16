from .conftest import ParserTestCase


class ListTestCase(ParserTestCase):
    def test_comment(self):
        wikitext = '<!-- This\nis\ncomment-->'
        self.assertParsed(wikitext, [])
