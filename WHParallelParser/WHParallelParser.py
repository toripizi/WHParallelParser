from bs4 import BeautifulSoup, element
from WHParallelParser.data import new_line_tags
from WHParallelParser.data import forbidden_tags
from WHParallelParser.api import MWApi
from WHParallelParser.Rules import RuleList


class WHParallelParser:
    def __init__(
        self,
        rules=RuleList(forbidden_tags),
        cache_folder="/tmp",
        URL="https://en.wikipedia.org/w/api.php",
    ):
        self.rules = rules
        self.api = MWApi(URL, cache_folder)
        self.parsed = None

    def parse_wikicode(self, text):
        soup = BeautifulSoup(self.api.parse(text), "html.parser")
        root = soup.find("div", {"class": "mw-parser-output"})
        self.parsed = ParserJob(root, self.rules)
        return self.parsed

    def parse_html(self, html):
        soup = BeautifulSoup(html, "html.parser")
        root = soup.find("div", {"class": "mw-parser-output"}) or soup.find()
        self.parsed = ParserJob(root, self.rules)
        return self.parsed


class ParserJob:
    def __init__(self, root, rules):
        self.rules = rules
        self.root = root
        self.preformatted = False
        self.text = [""]
        self.data = []
        self.textLocation = 0
        self.process(root)
        self.repair_text()

    def repair_text(self):
        if not self.text[-1]:
            self.text.pop()
        #self.text = [line.strip() for line in self.text]

    def process(self, section):
        {
            element.Tag: self.process_tag,
            element.NavigableString: self.process_string,
            element.Comment: lambda a: None,
        }[type(section)](section)

    def process_tag(self, tag):
        if self.rules.test(tag):
            return

        if tag.name in new_line_tags:
            if len(self.text[self.textLocation]) > 0:
                self.textLocation += 1
                self.text.append("")
        obj = {
            "tag": tag.name,
            "attrs": tag.attrs,
            "start": [self.textLocation, len(self.text[self.textLocation])],
        }
        if tag.name == "pre":
            self.preformatted = True

        for child in tag.children:
            self.process(child)

        if tag.name == "pre":
            self.preformatted = False

        obj["end"] = [self.textLocation, len(self.text[self.textLocation])]

        if tag.name in new_line_tags:
            if len(self.text[self.textLocation]) > 0:
                self.textLocation += 1
                self.text.append("")
        self.data.append(obj)

    def process_string(self, string):
        if self.preformatted:
            self.process_preformatted_string(string)
            return
        if string == "\n":
            return
        fixed_str = self.fix_string(string)
        self.text[self.textLocation] += fixed_str

    def process_preformatted_string(self, string):
        self.text[self.textLocation] += string

    def fix_string(self, string):
        string = string.replace("\r\n", " ")
        string = string.replace("\n", " ")
        while "  " in string:
            string = string.replace("  ", " ")
        if (
            self.text[self.textLocation]
            and self.text[self.textLocation][-1] == " "
            and string[0] == " "
        ):
            string = string[1:]
        return string

    def find_first_tag(self, expected_tag):
        for tag in self.data:
            if tag["tag"] == expected_tag:
                return tag
        return {"tag": None}
