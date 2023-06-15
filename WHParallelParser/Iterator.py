import json
import random
from WHParallelParser import WHParallelParser


class Iterator:
    def __init__(self, file_name):
        self.html_data = open(file_name, "rb")
        self.parser = WHParallelParser(cache_folder="./cached")
        self.lines = self.html_data.readlines()

    def __iter__(self):
        return self

    def __next__(self):
        idx = random.randint(0, len(self.lines))
        line = self.lines.pop(idx)
        if line:
            json_data = json.loads(line)
            return {
                "html": self.parser.parse_html(json_data["article_body"]["html"]),
                "data": json_data
            }
        raise StopIteration
