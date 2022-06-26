from .conftest import ParserTestCase


class RefTestCase(ParserTestCase):
    def test_basic(self):
        wikitext = "<ref></ref>"
        self.assertParsed(wikitext, [])

    def test_empty_tag(self):
        wikitext = "<ref />"
        self.assertParsed(wikitext, [])

    def test_empty_tag_no_space(self):
        wikitext = "<ref/>"
        self.assertParsed(wikitext, [])

    def test_empty_tag_with_attribute(self):
        wikitext = "<ref name=powierzchnia group=uwaga />"
        self.assertParsed(wikitext, [])

    def test_tag_with_attribute_and_content(self):
        wikitext = "<ref group=uwaga>Content</ref>"
        self.assertParsed(wikitext, [])

    def test_tag_with_attribute_and_links_in_content(self):
        wikitext = "<ref group=uwaga>Content with [[link]] and [[another link]]</ref>"
        self.assertParsed(wikitext, [])

    def test_tag_with_double_braces(self):
        wikitext = "<ref>{{cytuj stronę |url = https://www.cia.gov/library/publications/resources/the-world-factbook/rankorder/2147rank.html#pl |tytuł = Country comparison: Area |praca = The World Factbook |opublikowany = [[Centralna Agencja Wywiadowcza|Central Intelligence Agency]] |język = en |data dostępu = 2017-11-29}}</ref>"
        self.assertParsed(
            wikitext,
            [
                '^ "Country comparison: Area". The World Factbook. Central Intelligence Agency. Retrieved 2017-11-29.'
            ],
        )

    def test_content_after_ref(self):
        wikitext = "<ref>Content inside</ref>. Content outside."
        self.assertParsed(wikitext, [". Content outside.", "^ Content inside"])

    def test_ref_with_link_with_url_in_content(self):
        wikitext = "językowych<ref>[[stats:EN/TablesWikipediaZZ.htm|Http://stats.wikimedia.org/EN/TablesWikipediaZZ.htm]] Wikipedia Statistics All languages.</ref> something"
        self.assertParsed(
            wikitext,
            [
                "językowych something",
                "^ Http://stats.wikimedia.org/EN/TablesWikipediaZZ.htm Wikipedia Statistics All languages.",
            ],
        )
