import json
from WHParallelParser import WHParallelParser


class Iterator:
    def __init__(self, file_name):
        self.html_data = open(file_name, "rb")
        self.parser = WHParallelParser(cache_folder="./cached")

    def __iter__(self):
        return self

    def __next__(self):
        line = self.html_data.readline()
        if line:
            json_data = json.loads(line)
            return self.parser.parse_html(json_data["article_body"]["html"])
        raise StopIteration
