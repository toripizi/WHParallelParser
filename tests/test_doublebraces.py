from tests.conftest import ParserTestCase


class DoubleBracesTestCase(ParserTestCase):
    def test_basic(self):
        wikitext = '{{This will be deleted}}'
        self.assertParsed(wikitext, ['Template:This will be deleted'])

    def test_embeded(self):
        wikitext = '{{This <ref>{{This is a test}}</ref>}}'
        self.assertParsed(wikitext, ['{{This }}', '^ Template:This is a test'])

    def test_embeded2(self):
        wikitext = '{{This <ref> {{This is a test}}</ref>}}'
        self.assertParsed(wikitext, ['{{This }}', '^ Template:This is a test'])
