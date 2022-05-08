from src.api import MWApi
from bs4 import BeautifulSoup, element
from src.data import forbidden_tags, new_line_tags


class MWParser:
    def __init__(self, URL, cache_folder):
        self.api = MWApi(URL, cache_folder)
        self.parsed = None

    def parse_wikicode(self, text):
        soup = BeautifulSoup(self.api.parse(text), 'html.parser')
        root = soup.find("div", {"class": "mw-parser-output"})
        self.parsed = ParserJob(root)
        return self.parsed

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        root = soup.find()
        self.parsed = ParserJob(root)
        return self.parsed

    def get_text_from_tag(self):
        pass


class ParserJob:
    def __init__(self, root):
        self.root = root
        self.text = [""]
        self.data = []
        self.textLocation = 0
        self.process(root)

    def process(self, section):
        {
            element.Tag: self.process_tag,
            element.NavigableString: self.process_string,
            element.Comment: lambda a: None,
        }[type(section)](section)

    def process_tag(self, tag):
        # TODO zrefactorować to trzeba
        for forbidden_tag in forbidden_tags:
            if forbidden_tag["name"] == tag.name:
                match = True
                for name, value in forbidden_tag["attrs"].items():
                    if not (name in tag.attrs and tag.attrs[name] == value):
                        match = False
                if match:
                    return
        # TODO zrefactorować to trzeba

        if tag.name in new_line_tags:
            if len(self.text[self.textLocation]) > 0:
                self.textLocation += 1
                self.text.append("")
        obj = {
            "tag": tag.name,
            "attrs": tag.attrs,
            "start": [self.textLocation, len(self.text[self.textLocation])]
        }
        for child in tag.children:
            self.process(child)
        obj["end"] = [self.textLocation, len(self.text[self.textLocation])-1]
        self.data.append(obj)

    # def check_tag(self, tag):
    #     pass

    def process_string(self, string):
        if string == "\n":
            return
        fixed_str = self.fix_string(string)
        self.text[self.textLocation] += fixed_str

    @staticmethod
    def fix_string(string):
        string = string.replace("\r\n", " ")
        string = string.replace("\n", " ")
        # TODO maybe easier?
        while "  " in string:
            string = string.replace("  ", " ")
        return string
