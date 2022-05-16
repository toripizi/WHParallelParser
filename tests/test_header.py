import unittest
from .conftest import ParserTestCase


class HeaderTestCase(ParserTestCase):
    def test_basic(self):
        wikitext = '== Header ==\nContent'
        self.assertParsed(wikitext, ['Header', 'Content'])

    def test_header_not_on_the_begining(self):
        wikitext = 'Content1\n== Header ==\nContent2'
        self.assertParsed(wikitext, ['Content1', 'Header', 'Content2'])

    def test_no_spaces(self):
        wikitext = '==Header==\nContent'
        self.assertParsed(wikitext, ['Header', 'Content'])

    def test_extra_spaces(self):
        wikitext = '==  \tHeader     ==\nContent'
        self.assertParsed(wikitext, ['Header', 'Content'])

    def test_content_before_header(self):
        wikitext = 'Before == Header =='
        self.assertParsed(wikitext, ['Before == Header =='])

    def test_content_after_header(self):
        wikitext = '== Header == After'
        self.assertParsed(wikitext, ['== Header == After'])

    def test_with_tag_before_header(self):
        wikitext = '<center>Something</center>  == Header ==\n'
        self.assertParsed(wikitext, ['Something', '== Header =='])

    def test_with_tag_after_header(self):
        wikitext = '  == Header == <center>Something</center>\n'
        self.assertParsed(wikitext, ['== Header ==', 'Something'])

    def test_different_open_adn_close(self):
        """To fix it back references must work in regexps"""
        wikitext = '== Header ===\n'
        self.assertParsed(wikitext, ['Header ='])

    def test_level_4(self):
        wikitext = '==== Zabór rosyjski ====\nTekst'
        self.assertParsed(wikitext, ['Zabór rosyjski', 'Tekst'])

    def test_level_4_with_link(self):
        wikitext = '\n==== [[Departament zamorski|Departamenty zamorskie]] ====\nTekst'
        self.assertParsed(wikitext, ['Departamenty zamorskie', 'Tekst'])

    def test_header_with_ref_and_doublebraces(self):
        wikitext = '\n==== Filmografia<ref name=\"gs/mkg\">{{Cytuj stronę | url = ' \
                   'https://www.gniazdoswiatow.net/2012/07/20/mini-kompendium-ghibli/ | tytuł = Ghibli – Mini ' \
                   'kompendium | autor = [[Bartek Biedrzycki]] | praca = GniazdoSwiatow.net | data dostępu = ' \
                   '2017-02-03}}</ref> ====\nTekst '
        expected_text = ['Filmografia', 'Tekst', '^ Bartek Biedrzycki. "Ghibli – Mini kompendium". GniazdoSwiatow.net. '
                                        'Retrieved 2017-02-03.']
        self.assertParsed(wikitext, expected_text)
