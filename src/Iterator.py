import json
from MWParser import MWParser

f = open("test.txt", "a")


class Iterator:
    def __init__(self, file_name):
        self.html_data = open(file_name, "rb")
        self.parser = MWParser("./cached")

    def __iter__(self):
        return self

    def __next__(self):
        line = self.html_data.readline()
        json_data = json.loads(line)
        return self.parser.parse_html(json_data["article_body"]["html"])


for html in Iterator("../simplewiki_0.ndjson"):
    print(html.text)
