from .conftest import ParserTestCase


class WikilinkTestCase(ParserTestCase):
    def test_link(self):
        wikitext = "[[hipertekst]] something"
        tags = {
            "tag": "a",
            "attrs": {
                "href": "/w/index.php?title=Hipertekst&action=edit&redlink=1",
                "class": ["new"],
                "title": "Hipertekst (page does not exist)",
            },
            "start": [0, 0],
            "end": [0, 9],
        }
        self.assertTags(wikitext, tags, "a")

    def test_files_removal(self):
        wikitext = "[[Plik:Jan Matejko, Stańczyk.jpg|mały|lewo|[[Jan Matejko]], ''[[Stańczyk (obraz Jana Matejki)|Stańczyk]]'']]"
        tags = {
            "tag": "a",
            "attrs": {"href": "/wiki/Jan_Matejko", "title": "Jan Matejko"},
            "start": [0, 43],
            "end": [0, 53],
        }
        self.assertTags(wikitext, tags, "a")

    def test_blend_link(self):
        wikitext = "[[klasycyzm]]em"
        tags = {
            "tag": "a",
            "attrs": {
                "href": "/w/index.php?title=Klasycyzm&action=edit&redlink=1",
                "class": ["new"],
                "title": "Klasycyzm (page does not exist)",
            },
            "start": [0, 0],
            "end": [0, 10],
        }
        self.assertTags(wikitext, tags, "a")

    def test_blend_link_in_quotes(self):
        wikitext = '"[[hipertekst]]" something'
        tags = {
            "tag": "a",
            "attrs": {
                "href": "/w/index.php?title=Hipertekst&action=edit&redlink=1",
                "class": ["new"],
                "title": "Hipertekst (page does not exist)",
            },
            "start": [0, 1],
            "end": [0, 10],
        }
        self.assertTags(wikitext, tags, "a")

    def test_blend_link_in_round_brackets(self):
        wikitext = "([[1971]]) something"
        tags = {
            "tag": "a",
            "attrs": {"href": "/wiki/1971", "title": "1971"},
            "start": [0, 1],
            "end": [0, 4],
        }
        self.assertTags(wikitext, tags, "a")

    def test_blend_link_with_polish_chars(self):
        wikitext = "[[ąę]]żźćółąę something"
        tags = {
            "tag": "a",
            "attrs": {
                "href": "/w/index.php?title=%C4%84%C4%99&action=edit&redlink=1",
                "class": ["new"],
                "title": "Ąę (page does not exist)",
            },
            "start": [0, 0],
            "end": [0, 1],
        }
        self.assertTags(wikitext, tags, "a")

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
        tags = {
            "tag": "a",
            "attrs": {"href": "/wiki/Flute", "title": "Flute"},
            "start": [0, 0],
            "end": [0, -1],
        }
        self.assertTags(wikitext, tags, "a")
