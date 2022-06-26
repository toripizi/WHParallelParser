from WHParallelParser import WHParallelParser
from WHParallelParser import Iterator
from WHParallelParser import Rule

path_to_html = "./example.html"
path_to_simplewiki = "example_simplewiki.json/simplewiki.ndjson"
cache_folder = "./cached"


# parser initialization, we should specify cache_folder
parser = WHParallelParser(cache_folder=cache_folder)

# parsing html
with open(path_to_html, "r") as file:
    output = parser.parse_html(file)
    print(output.text)
    print(output.data)

# parsing wikicode
output = parser.parse_wikicode("[[link]]")
print(output.text)
print(output.data)

# we can iterate over simplewiki json file
for html in Iterator(path_to_simplewiki):
    print(html.text)

# RULES
# we can add some rules
parser.rules.add_rule(Rule({"name": "a", "class": "mw-disambig"}))

output = parser.parse_wikicode("[[link]] '''test'''")
print(output.text)
print(output.data)

# we can remove some rules
parser.rules.remove_rule(Rule({"name": "a", "class": "mw-disambig"}))

output = parser.parse_wikicode("[[link]] '''test'''")
print(output.text)
print(output.data)
