from .conftest import ParserTestCase


class WikilinkTestCase(ParserTestCase):
    def test_link(self):
        wikitext = "[[hipertekst]] something"
        tags = [
            {
                "tag": "a",
                "attrs": {"href": "hipertekst"},
                "text": [{"line": 0, "start": 0, "length": 10}],
            }
        ]
        self.assertParsed(wikitext, ["hipertekst something"], tags)

    def test_files_removal(self):
        wikitext = "[[Plik:Jan Matejko, Stańczyk.jpg|mały|lewo|[[Jan Matejko]], ''[[Stańczyk (obraz Jana Matejki)|Stańczyk]]'']]"
        self.assertParsed(
            wikitext,
            ["[[Plik:Jan Matejko, Stańczyk.jpg|mały|lewo|Jan Matejko, Stańczyk]]"],
        )

    def test_blend_link(self):
        wikitext = "[[klasycyzm]]em"
        tags = [
            {
                "tag": "a",
                "attrs": {"href": "klasycyzm"},
                "text": [{"line": 0, "start": 0, "length": 11}],
            }
        ]
        self.assertParsed(wikitext, ["klasycyzmem"], tags)

    def test_blend_link_in_quotes(self):
        wikitext = '"[[hipertekst]]" something'
        tags = [
            {
                "tag": "a",
                "attrs": {"href": "ąę"},
                "text": [{"line": 0, "start": 1, "length": 10}],
            }
        ]
        self.assertParsed(wikitext, ['"hipertekst" something'], tags)

    def test_blend_link_in_round_brackets(self):
        wikitext = "([[1971]]) something"
        tags = [
            {
                "tag": "a",
                "attrs": {"href": "1971"},
                "text": [{"a": 0, "start": 1, "length": 4}],
            }
        ]
        self.assertParsed(wikitext, ["(1971) something"], tags)

    def test_blend_link_with_polish_chars(self):
        wikitext = "[[ąę]]żźćółąę something"
        tags = [
            {
                "tag": "a",
                "attrs": {"href": "ąę"},
                "text": [{"line": 0, "start": 0, "length": 9}],
            }
        ]
        self.assertParsed(wikitext, ["ąężźćółąę something"], tags)

    def test_titled_link(self):
        wikitext = "[http://example.com I am a link]."
        self.assertParsed(wikitext, ["I am a link."])

    def test_titled_link_with_utf8(self):
        wikitext = "[http://example.com Żółć]."
        self.assertParsed(wikitext, ["Żółć."])

    def test_titled_link_without_ending_bracket(self):
        wikitext = "some <ref>[http://example.com It should work by now</ref>content [[and link]]."
        self.assertParsed(
            wikitext,
            ["some content and link.", "^ [http://example.com It should work by now"],
        )

    def test_blend_link_in_file_link(self):
        wikitext = "[[File:true.berries.jpg|300px|thumb|right|[[grape]]s]]"
        self.assertParsed(wikitext, ["grapes"])

    def test_invalid_link_multiline(self):
        wikitext = "[[kinematics\n]]"
        self.assertParsed(wikitext, ["[[kinematics ]]"])

    def test_link_to_score(self):
        wikitext = r"""[[flute|<score vorbis="1"> \relative c''''  { \clef treble \time 4/4 \set Staff.midiInstrument = #"flute"  \tempo "Allegro" 4=176 \slashedGrace a8\mf( g8-.)[ e-.] \slashedGrace a( gis-.)[ gis-.] gis-.[ gis-.] \slashedGrace a( gis-.)[ e-.] | d16->( ees des c b8) \times 2/3 {a16( b a } g8->) g-. c-. e-. | \slashedGrace a8( g8-.)[ e-.] \slashedGrace a( gis-.)[ gis-.] gis-.[ gis-.] \slashedGrace a( gis-.)[ e-.] | d16->( ees des c g'!8-.) \slashedGrace b,( a-.) g2-> } </score>]]"""
        tags = [
            {
                "tag": "a",
                "attrs": {"href": "flute"},
                "text": [{"line": 0, "start": 0, "length": 5}],
            }
        ]
        self.assertParsed(wikitext, ["flute"], tags)
