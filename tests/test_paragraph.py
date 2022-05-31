from .conftest import ParserTestCase
import unittest


class ParagraphTestCase(ParserTestCase):
    def test_basic(self):
        wikitext = "This is a paragraph\n\nThis is next"
        self.assertParsed(wikitext, ["This is a paragraph", "This is next"])

    def test_ident_text(self):
        wikitext = "This is a paragraph\n:This is next"
        self.assertParsed(wikitext, ["This is a paragraph", "This is next"])

    def test_bullet_list(self):
        wikitext = "This is a paragraph\n* This is next\n** And That"
        self.assertParsed(wikitext, ["This is a paragraph", "This is next", "And That"])

    def test_numbered_list(self):
        wikitext = "This is a paragraph\n# This is next\n## And That"
        self.assertParsed(wikitext, ["This is a paragraph", "This is next", "And That"])

    def test_definition_list(self):
        wikitext = "This is a paragraph\n; This is next\n: And That"
        self.assertParsed(wikitext, ["This is a paragraph", "This is next", "And That"])

    def test_glue_to_paragraph(self):
        wikitext = "This is a paragraph\nthis is continuation"
        self.assertParsed(wikitext, ["This is a paragraph this is continuation"])

    def test_extra_newlines(self):
        wikitext = "This is a paragraph\n\n{{some template}}\n\nThis is next"
        self.assertParsed(
            wikitext, ["This is a paragraph", "Template:Some template", "This is next"]
        )

    def test_extra_spaces_between_words(self):
        wikitext = "This     is     a paragraph"
        self.assertParsed(wikitext, ["This is a paragraph"])

    def test_spaces_at_the_begin_of_paragraph(self):
        """This will not work when preformatted paragraph will be implemented."""
        wikitext = " This     is     a paragraph"
        self.assertParsed(wikitext, ["This is a paragraph"])

    def test_extra_spaces_between_words_with_formatting(self):
        wikitext = "This     '''is     '''a paragraph"
        self.assertParsed(wikitext, ["This is a paragraph"])

    def test_extra_spaces_between_words_with_links(self):
        wikitext = "This     [[ is    a ]] paragraph"
        self.assertParsed(wikitext, ["This is a paragraph"])

    def test_extra_spaces_between_words_with_links2(self):
        wikitext = "[[ Test ]] This     [[ is    a ]] paragraph [[ Another ]]"
        self.assertParsed(wikitext, ["Test This is a paragraph Another"])

    def test_extra_spaces_between_words_with_links3(self):
        wikitext = "[[ Test ]]     [[ Another ]]"
        self.assertParsed(wikitext, ["Test Another"])

    @unittest.skip
    def test_preformatted_paragraph(self):
        wikitext = "  This     is     a paragraph"
        self.assertParsed(wikitext, ["This     is     a paragraph"])

    @unittest.skip
    def test_preformatted_paragraph_with_markup(self):
        wikitext = "  This     is     a '''paragraph'''"
        self.assertParsed(wikitext, ["This     is     a paragraph"])

    @unittest.skip
    def test_preformatted_multi_paragraph(self):
        wikitext = " This     is     a paragraph\n  There are two spaces!"
        self.assertParsed(
            wikitext, ["This     is     a paragraph", " There are two spaces!"]
        )

    @unittest.skip
    def test_preformatted_and_standard_paragraph_after(self):
        wikitext = " This     is     a paragraph\nThis    is   standard"
        self.assertParsed(wikitext, ["This     is     a paragraph", "This is standard"])
